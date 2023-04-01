from utilities.readProperties import ReadConfig
import time
from Configurations.config import TestData
from pageObjects.LoginPage2 import LoginPage2
import sys


class Test_Bkash:
    baseURL = ReadConfig.getApplicationURLBkash()

    # pytest -v -s --alluredir="C:\Users\hp\PycharmProjects\Selenium_Python_POM_Framework\report" testCases/test_bkash.py --browser chrome

    def test_bkashurlopen(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.driver.close()

    def test_hubspot(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)
        time.sleep(3)
        self.lp = LoginPage2(self.driver)
        time.sleep(2)
        title = self.lp.get_login_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE
        time.sleep(2)
        flag = self.lp.is_signup_link_exists()
        assert flag
        time.sleep(2)
        self.lp.do_login(TestData.USER_NAME, TestData.PASSWORD)
        time.sleep(3)
        self.driver.close()

    def test_title2(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(TestData.BASE_URL)
        time.sleep(3)
        self.lp = LoginPage2(self.driver)
        time.sleep(3)
        title2 = self.lp.get_title__2()
        print(title2)
        assert title2 == TestData.LOGIN_PAGE_TITLE
        self.driver.close()
