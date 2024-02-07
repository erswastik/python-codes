from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Set the path to your ChromeDriver executable
chromedriver_path = "C:\\Users\\Admin\\Desktop\\driver\\chromedriver.exe"

# Set the path to the image you want to upload
image_path = "C:\\Users\\Admin\\Desktop\\post\\lion.jpg"

# Instagram login credentials
username = "namasteguru007"
password = "Swastik@7408"

# Start the ChromeDriver
driver = webdriver.Chrome()

# Open Instagram
driver.get("https://www.instagram.com")

# Wait for the page to load
time.sleep(12)

# Find and fill the login form
username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")
username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)

# Wait for the login to complete
time.sleep(10)

# Dismiss the "Save Login Info" prompt, if it appears
try:
    driver.find_element_by_xpath("//button[text()='Not Now']").click()
except:
    pass

# Dismiss the "Turn on Notifications" prompt, if it appears
try:
    driver.find_element_by_xpath("//button[text()='Not Now']").click()
except:
    pass

# Click on the "Create Post" button
driver.find_element(By.CLASS_NAME, "x1n2onr6 x6s0dn4 x78zum5").click()

# Wait for the post creation page to load
time.sleep(8)

# Find the file input and upload the image
file_input = driver.find_element(By.XPATH, "//input[@type='file']")
file_input.send_keys(image_path)

# Wait for the image to upload
time.sleep(8)

# Find and click the "Next" button
driver.find_element(By.XPATH, "//button[text()='Next']").click()

# Wait for the next page to load
time.sleep(8)

# Add a caption (optional)
caption_input = driver.find_element(By.XPATH, "//textarea[@aria-label='Write a caption…']")
caption_input.send_keys("#lion #wildlife")

# Find and click the "Share" button
driver.find_element(By.XPATH, "//button[text()='Share']").click()

# Wait for the post to be uploaded
time.sleep(60)

# Close the browser

