from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
import time

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service = service)
cookiePath = "https://orteil.dashnet.org/cookieclicker/"
driver.get(cookiePath)

sign_in_language = '//*[@id="langSelect-EN"]'
driver.implicitly_wait(5)
sign_in_button=driver.find_element(By.XPATH,sign_in_language)
print(sign_in_button)
sign_in_button.click()
driver.implicitly_wait(10)
big_cookie_xpath = '//*[@id="bigCookie"]'
big_cookie = driver.find_element(By.XPATH,big_cookie_xpath)
for x in range(0,1000):   

    big_cookie.click()
    curser_xpath = '//*[@id="product0"]'
    curser = driver.find_element(By.XPATH,curser_xpath)
    curser.click()

curser_xpath = '//*[@id="product0"]'
curser = driver.find_element(By.XPATH,curser_xpath)
curser.click()
time.sleep(10)
if __name__=="__main__":
    pass