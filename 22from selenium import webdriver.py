from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time 

# Set the path to your ChromeDriver executable
chromedriver_path = r"C:\Users\Admin\Desktop\driver\chromedriver.exe"

# Set the Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:\\Users\\Admin\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")

# Create the ChromeDriver service
service = Service(chromedriver_path)

# Start the ChromeDriver with options
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Instagram
driver.get("https://www.instagram.com")

# Rest of your code...
time.sleep(20)