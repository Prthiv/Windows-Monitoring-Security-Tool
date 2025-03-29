=========================================
 Windows Monitoring & Security Tool
=========================================

A powerful tool to monitor your Windows laptop and detect unauthorized access.  
This tool runs in the background and sends a **webcam photo** to your **Discord bot**  
when someone turns on your laptop without your knowledge.  

-------------------------------
🔹 Features:
-------------------------------
✅ **Startup Notification** – Sends an alert with a webcam photo when the laptop is powered on.  
✅ **Remote Control via Discord** – Control your laptop remotely with these commands:

📷 `!camera` – Capture a webcam photo  
ℹ️ `!help` – Show this help message  
🔄 `!restart` – Restart the laptop  
🖼️ `!screenshot` – Take a screenshot  
💻 `!shell` – Execute a shell command remotely  
⏻ `!shutdown` – Shutdown the laptop  
⏹️ `!stop` – Stop any ongoing process  

-------------------------------
🔹 How to Convert to EXE:
-------------------------------
1. Install **PyInstaller**:  
pip install pyinstaller

vbnet
Copy
Edit
2. Open a terminal in the script's directory and run:  
pyinstaller --noconsole --onefile script.py

markdown
Copy
Edit
- `--noconsole`: Hides the console window.  
- `--onefile`: Packs everything into a single `.exe` file.  
3. The `.exe` file will be in the `dist` folder.  

-------------------------------
🔹 How to Run at Startup:
-------------------------------
1. Press `Win + R`, type:  
shell:startup

pgsql
Copy
Edit
and press **Enter**.  
2. Move the generated `.exe` file into this folder.  
3. The program will now start automatically whenever the laptop turns on.  

🚀 Built with Python & Discord API  
This ensures the bot runs stealthily and starts automatically. Let me know if you need any modifications! 🚀
