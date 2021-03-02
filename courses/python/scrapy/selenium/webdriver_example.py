from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

import time 

def chrome_webdriver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://books.toscrape.com/')
    time.sleep(2)
    driver.quit()

def chromium_webdriver():
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver.get('https://books.toscrape.com/')
    time.sleep(2)
    driver.quit()

def firefox_webdriver():
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get('https://books.toscrape.com/')
    time.sleep(2)
    driver.quit()


# Not even bothering with edge shit 

def opera_webdriver():
    """
    Work like shit. 
    """
    driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    driver.get('https://books.toscrape.com/')
    time.sleep(2)
    driver.quit()

# chrome_webdriver()
# chromium_webdriver()
# firefox_webdriver()
# opera_webdriver()
