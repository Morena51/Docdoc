import pytest
from selenium import webdriver

@pytest.fixture()
def setUp():
    driver = webdriver.Chrome('C:/Users/User/Documents/DocDoc/Autotesting/chromedriver.exe')
    driver.get("https://shop.docdoc.ru/")