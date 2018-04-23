import unittest
import selenium
import selenium.webdriver.support
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

def check_xpath(text):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, text))
        )
    except TimeoutException:
        print('TimeoutException')
    except NoSuchElementException:
        print('NoSuchElementException')

def check_name(text):
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, text))
        )
    except TimeoutException:
        print('TimeoutException')
    except NoSuchElementException:
        print('NoSuchElementException')       
phone=1111111111
button_send='//button'
driver = webdriver.Chrome('C:/Users/User/Documents/DocDoc/Autotesting/chromedriver.exe')
driver.get("https://shop.docdoc.ru/")
# заходим на страницу логина
driver.find_element_by_link_text('Войти').click()
# вводим номер телефона
driver.find_element_by_xpath('//input').send_keys(phone)
driver.find_element_by_xpath(button_send).click()
# вводим код авторизации
check_name("code")
elem=driver.find_element_by_name("code")
elem.send_keys("5555")
elem.send_keys(Keys.RETURN)
#отправляем код авторизации
check_xpath('//button[@value="Подтвердить"]')
try:
    driver.find_element_by_xpath('//button[@value="Подтвердить"]').click()
except NoSuchElementException:
        print('NoSuchElementException')
driver.close()