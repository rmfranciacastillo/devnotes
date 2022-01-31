from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_name = "username"
password = "password"

# Creating a chromedriver instance
driver = webdriver.Chrome()  # For Chrome
#driver = webdriver.Firefox() # For Firefox

# Opening facebook homepage
driver.get("https://www.facebook.com")

# Identifying email and password textboxes
email = driver.find_element_by_id("email")
passwd = driver.find_element_by_id("pass")

# Sending user_name and password to corresponding textboxes
email.send_keys(user_name)
passwd.send_keys(password)

# Sending a signal that RETURN key has been pressed
passwd.send_keys(Keys.RETURN)

# driver.quit()
