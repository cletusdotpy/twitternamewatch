import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

def send_text():
    options = webdriver.ChromeOptions()
    options.add_argument(r'CHROME DATA DIRECTORY HERE') #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data  - This and below use Chrome data to allow automatic login to Google Voice
    options.add_argument(r'YOUR DESIRED CHROME PROFILE') #e.g. Profile 3

    driver = webdriver.Chrome(options=options)
    driver.get('https://voice.google.com/u/0/messages')
    search = driver.find_element(By.CLASS_NAME, 'gvMessagingView-actionButton') # New message button
    search.send_keys(Keys.RETURN)
    search = driver.find_element(By.ID, 'input_0') # Input field for message recipient
    search.send_keys("YOUR PHONE NUMBER HERE")
    search.send_keys(Keys.RETURN)
    search = driver.find_element(By.ID, 'input_1') # Input field for message text
    search.send_keys("Twitter Username Available! Act now scrub")
    search.send_keys(Keys.RETURN)

if __name__ == '__main__':
    send_text()
