# **Windows Monitoring & Security Tool**  

A **stealthy Windows monitoring tool** that **alerts you via Discord** when someone turns on your laptop.  
It also allows **remote control** through Discord commands.  

---

## 📌 **Features**  

✔ **Startup Notification** – Sends an alert with a **webcam photo** when the laptop is turned on.  
✔ **Remote Control via Discord** – Execute commands remotely, including:  

```
!camera      → Capture a webcam photo  
!screenshot  → Take a screenshot  
!shell <cmd> → Execute shell commands remotely  
!shutdown    → Shutdown the laptop  
!restart     → Restart the laptop  
!stop        → Stop any ongoing process  
!help        → Show help message  
```

✔ **Runs in Background** – Fully hidden execution (no visible console window).  
✔ **Automatic Startup** – Runs automatically **when Windows starts**.  

---

## ⚡ **Installation**  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/Prthiv/Windows-Monitoring-Security-Tool.git
cd Windows-Monitoring-Security-Tool
```
2️⃣ **Install dependencies** (Python 3 required)  
```bash
pip install -r requirements.txt
```
3️⃣ **Edit the script with your credentials**  
- Open `script.py` and replace `TOKEN = ""` with your **Discord bot token**.  
- Replace `OWNER_ID = ` with your **Discord user ID**.  

4️⃣ **Run the script**  
```bash
python script.py
```
- The bot will start in the background and **notify you when the laptop turns on**.  

---

## 🔄 **Convert Script to EXE (Windows Only)**  

To run the tool **without requiring Python**, convert it to a `.exe` file:  

1️⃣ **Install PyInstaller**  
```bash
pip install pyinstaller
```
2️⃣ **Convert the script to EXE**  
Run this command in the project directory:  
```bash
pyinstaller --noconsole --onefile script.py
```
✔ `--noconsole` → Hides the console window (runs stealthily).  
✔ `--onefile` → Generates a **single `.exe` file** inside the `dist` folder.  

---

## 🔧 **Set the EXE to Run at Startup (Windows Only)**  

To **make the program start automatically** when Windows boots up:  

1️⃣ **Open Windows Startup Folder**  
- Press `Win + R`, type:  
  ```
  shell:startup
  ```
  and press **Enter**.  

2️⃣ **Move the EXE to Startup Folder**  
- Go to the `dist` folder inside your project directory.  
- Copy the generated `.exe` file.  
- Paste it inside the **Startup** folder.  

3️⃣ **Restart Your Laptop**  
Now, the tool will **run automatically in the background** every time Windows starts. 🚀  

---

## 📜 **Disclaimer**  

🔹 **This tool is for educational and security purposes only**.  
🔹 **Do not use it for unethical activities**.  

---

💻 **Developed with Python & Discord API** 🚀  
