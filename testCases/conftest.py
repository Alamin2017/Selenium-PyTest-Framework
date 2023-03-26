from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture()
def setup(browser):
    if browser == "chrome":

        option = Options()
        option.add_argument('--disable-notifications')
        s = Service("E:\Soft\Python_PyCharm\chromedriver.exe")
        driver = webdriver.Chrome(service=s, options=option)

        # option = Options()
        # option.add_argument('--disable-notifications')
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=option)

        print("Launching Chrome Browser")
        return driver
    elif browser == 'firefox':
        s = Service("E:\Soft\Python_PyCharm\geckodriver.exe")
        driver = webdriver.Firefox(service=s)

        # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        print("Launching Firefox Browser")
        return driver
    else:
        s = Service("E:\Soft\Python_PyCharm\msedgedriver.exe")
        driver = webdriver.Edge(service=s)

        # driver = webdriver.Edge(EdgeChromiumDriverManager().install())

        print("Launching Edge Browser")
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
