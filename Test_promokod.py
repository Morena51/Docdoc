import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def check_xpath(text):
    WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.XPATH, text))
    )

def check_name(text):
    WebDriverWait(driver, 120).until(
        EC.element_to_be_clickable((By.NAME, text))
    )
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
driver.find_element_by_xpath('//button[@value="Подтвердить"]').click()
driver.close()
