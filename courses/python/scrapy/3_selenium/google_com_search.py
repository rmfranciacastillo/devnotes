from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

search_term = 'dog'

driver = webdriver.Firefox()
driver.get("https://www.google.com")

assert "Google" in driver.title

# Identify Search Box and Search button
search = driver.find_element_by_name('q')

# Shows the source of the page
# print(driver.page_source)

# Search for dogs
search.send_keys(search_term)

# Search by pressing ENTER
search.send_keys(Keys.RETURN)

# Search images
images_link = driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a')

images_link.click()

# quit driver after 10 seconds
time.sleep(3)
driver.quit()
