from utilities.readProperties import ReadConfig
import time
import allure



class Test_Bkash:
    baseURL = ReadConfig.getApplicationURLBkash()
    #pytest -v -s --alluredir="C:\Users\hp\PycharmProjects\Selenium_Python_POM_Framework\report" testCases/test_bkash.py --browser chrome

    def test_urlopen(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(3)

