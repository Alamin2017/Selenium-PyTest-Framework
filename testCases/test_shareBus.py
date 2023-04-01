from utilities.readProperties import ReadConfig
from pageObjects.ShareBusPage import ShareBusPage
import time


class Test_ShareBus:
    baseURL = ReadConfig.getApplicationURL2()
    #pytest -v -s testCases/test_bkash.py --browser chrome --html=my_report.html


    def test_just(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(2)
        self.lp = ShareBusPage(self.driver)
        self.lp.ClickSignInButton()
        self.lp.enterEmail("brainstation23@yopmail.com")
        self.lp.enterPass("Pass@1234")
        time.sleep(3)
        self.lp.clickLoginInButton()
        time.sleep(8)
        self.driver.close()
