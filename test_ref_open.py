import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
# run after test
#@pytest.yield_fixture()

def test_contact():
    driver = webdriver.Chrome('C:/Users/User/Documents/DocDoc/Autotesting/chromedriver.exe')
    driver.get("https://shop.docdoc.ru/")
    driver.find_element_by_link_text("Контакты").click()
    #driver.switch_to.window(driver.window_handles[1])
    assert driver.find_element_by_xpath('//h1')=="Контакты"
    driver.close()

def test_user__agreement():
    driver = webdriver.Chrome('C:/Users/User/Documents/DocDoc/Autotesting/chromedriver.exe')
    driver.get("https://shop.docdoc.ru/")
    try:
        driver.find_element_by_link_text("Пользовательское соглашение").click()
    except :
        print("not found")
    driver.close()
