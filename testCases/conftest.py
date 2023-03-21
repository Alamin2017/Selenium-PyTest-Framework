from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        s = Service("E:\Soft\Python_PyCharm\chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        print("Launching Chrome Browser")
        return driver
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path='D:\Soft\Python_Selenium\Firefox\geckodriver.exe')
        print("Launching Firefox Browser")
        return driver
    else:
        driver = webdriver.Edge(executable_path='D:\Soft\Python_Selenium\Edge\msedgedriver.exe')
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
