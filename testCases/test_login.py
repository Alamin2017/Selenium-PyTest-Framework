import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class Test_001_login:
    # terminal test run
    # pytest -v -s testCases/test_login.py
    # pytest -v -s testCases/test_login.py --browser chrome
    # pytest -v -s -n=2 testCases/test_login.py --browser chrome
    # pytest -v -s -n=2 --html=reports/report.html testCases/test_login.py --browser chrome
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    baseURL2 = ReadConfig.getApplicationURL2()

    def test_homePageTitle(self, setup):

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_title.png")
            self.driver.close()
            assert False

    def test_login(self, setup):

        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        # self.lp.setUserName(self.username)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title1 = self.driver.title

        if act_title1 == "Dashboard / nopCommerce administration":

            assert True
            time.sleep(3)
            self.lp.clickLogout()
            time.sleep(3)
            self.driver.close()


        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_page_title.png")
            self.driver.close()
            assert False
