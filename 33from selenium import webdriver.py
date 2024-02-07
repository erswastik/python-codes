import subprocess
import time

# Set the path to your Chrome executable
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Set the profile directory
profile_directory = r"C:\Users\Admin\AppData\Local\Google\Chrome\User Data\Profile 2"

# Launch Chrome with the specified user profile
subprocess.Popen([chrome_path, "--user-data-dir=" + profile_directory])

# Wait for the browser to open and load the profile
time.sleep(5)

# Rest of your code...
