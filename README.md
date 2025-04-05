
# 🛡️ Windows Laptop Monitoring Tool

A **stealthy monitoring tool for Windows laptops** that notifies you via **Discord** when your system turns on, captures a **webcam photo**, and gives you **remote control** using **Discord Slash Commands**.

Ideal for **parental control**, **laptop protection**, or **personal remote monitoring**.

---

## 📌 Features

✔ **Startup Notification**  
- Automatically sends a message to your Discord with a **webcam photo** when the laptop is turned on.

✔ **Slash Command Control via Discord**  
Use Discord’s slash commands to control your laptop in real-time:

```
/screenshot   → Capture a screenshot of the desktop  
/camera       → Take a photo from the webcam  
/shutdown     → Shutdown the laptop  
/restart      → Restart the laptop  
/clear        → Delete all messages from the bot's DM  
/help         → Show all available commands  
/stop         → Stop the bot remotely  
```

✔ **Owner-Only Control**  
- Critical commands like `/shutdown`, `/restart`, `/clear`, and `/stop` are **restricted to the owner's Discord ID only**.

✔ **Automatic Screenshot & Webcam Support**  
- Captures screen and webcam even if you're not around.

✔ **Background Logging**  
- All events, errors, and actions are logged in `monitor.log`.

✔ **Runs Hidden**  
- Designed to run silently without any visible console window (convert to `.exe` for stealth).

---

## ⚙️ Installation

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/Laptop-Monitoring-Bot.git
cd Laptop-Monitoring-Bot
```

2️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

> `requirements.txt` should contain:
```
discord.py
opencv-python
pyautogui
mss
pillow
```

3️⃣ **Edit the Script**
- Open the script and replace the following:

```python
TOKEN = ""       # Your Discord Bot Token
OWNER_ID =       # Your Discord User ID (as an integer)
```

4️⃣ **Run the Script**
```bash
python bot.py
```

The bot will start and **send you a webcam snapshot after 15 seconds**.

---

## 🔒 Convert to EXE (Optional for Windows)

To make it run stealthily (no console popup), convert the script to a `.exe`:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile bot.py
```

✔ Output will be in the `dist` folder  
✔ Run the `.exe` to start the bot without a console window

---

## 🚀 Auto-Start on Windows Boot (Optional)

1. Press `Win + R` and type:
```
shell:startup
```

2. Copy your generated `.exe` from `dist/` into this folder.  
🔁 Your monitoring bot will now **auto-start** every time Windows boots.

---

## ⚠️ Disclaimer

This tool is built for **educational, personal monitoring, and laptop security purposes** only.  
Do **not** use it for malicious or unauthorized surveillance.

---

💻 Developed with Python + Discord API  
🎯 Secure. Stealthy. Smart.

