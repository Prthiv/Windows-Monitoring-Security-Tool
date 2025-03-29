Windows Monitoring & Security Tool
A powerful tool to monitor your Windows laptop and detect unauthorized access.
It runs stealthily in the background and notifies you via Discord when your laptop is turned on.
Additionally, it allows you to remotely control your laptop using Discord commands.

⚡ Features
✅ Startup Notification – Captures a webcam photo and sends an alert to Discord when the laptop is turned on.
✅ Remote Control via Discord – Use commands to control your laptop remotely:

Command	Description
!camera	Capture a webcam photo
!screenshot	Take a screenshot of the screen
!shell <command>	Execute a shell command remotely
!shutdown	Shut down the laptop
!restart	Restart the laptop
!stop	Stop any ongoing process
!help	Show help message with available commands
✅ Runs in Background – No visible console window, hidden execution.
✅ Easy to Set Up – Convert to .exe and run automatically on startup.

🚀 Installation
Clone the repository or download the script:

bash
Copy
Edit
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Install dependencies (Python 3 required):

bash
Copy
Edit
pip install -r requirements.txt
Set up your credentials:

Open .env and add your Discord bot token and channel ID.

Make sure your bot has administrator permissions on your Discord server.

Run the script:

bash
Copy
Edit
python script.py
The script will start in the background and notify you via Discord when the laptop turns on.

🔄 Convert Script to EXE (Windows Only)
To run the tool without requiring Python installed:

Step 1: Install PyInstaller
Open Command Prompt and install PyInstaller:

bash
Copy
Edit
pip install pyinstaller
Step 2: Convert Python Script to EXE
Run this command in the same folder as script.py:

bash
Copy
Edit
pyinstaller --noconsole --onefile --hidden-import=pkg_resources script.py
--noconsole → Hides the console window (runs stealthily).

--onefile → Creates a single .exe instead of multiple files.

--hidden-import=pkg_resources → Fixes missing dependencies issue.

After this, the .exe file will be generated inside the dist folder.

🔧 Set the EXE to Run at Startup (Windows Only)
To make the program run automatically when Windows starts:

Step 1: Open the Startup Folder
Press Win + R, type:

makefile
Copy
Edit
shell:startup
and press Enter. This will open the Startup folder.

Step 2: Move the EXE to Startup
Go to the dist folder inside your project directory.

Copy the generated .exe file.

Paste it inside the Startup folder.

Step 3: Restart Your Laptop
Now, whenever the laptop starts, the tool will run silently in the background. 🚀

📜 License
This project is for educational and security purposes only. Use it responsibly.

