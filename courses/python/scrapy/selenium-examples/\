from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

# driver path
DRIVER_PATH = './chromedriver'

#setup driver
driver = webdriver.Chrome(DRIVER_PATH) 

# Get website
# driver.get('https://www.markuptag.com/demo/javascript-load-more-content-on-click-button.php')
driver.get('https://www.udemy.com/courses/finance-and-accounting/')

# Click on the load more button
try:
    button = WebDriverWait(driver, 3).until(
        # EC.presence_of_element_located((By.ID, "loadmore"))
        EC.presence_of_element_located((By.CLASS_NAME, "pagination--next--5NrLo"))
    )
    print(button)
    button.click()

    time.sleep(10)

finally:
    driver.quit()
