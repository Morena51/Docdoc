import selenium
import selenium.webdriver.support
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException

def test_wait_300_sec():
    phone=1111111111
    button_send='//button'
    driver = webdriver.Chrome('C:/Users/User/Documents/DocDoc/Autotesting/chromedriver.exe')
    driver.get("https://shop.docdoc.ru/")
    # заходим на страницу логина
    driver.find_element_by_link_text('Войти').click()
    # вводим номер телефона
    driver.find_element_by_xpath('//input').send_keys(phone)
    driver.find_element_by_xpath(button_send).click()
    time.sleep(301)
    driver.find_element_by_xpath('//button[text()="Отправить код повторно"]').click()