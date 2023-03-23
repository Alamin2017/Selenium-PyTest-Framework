import time
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities import XLUtils


class Test_002_DDT_login:
    # terminal test run
    # pytest -v -s testCases/test_login_ddt.py --browser chrome
    # pytest -v -s -n=2 --html=reports/report.html testCases/test_login.py --browser chrome
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows i a Excel:", self.rows)
        lst_status = []
        for r in range(2, self.rows + 1):
            self.driver.implicitly_wait(5)
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            time.sleep(2)
            self.lp.setUserName(self.user)
            time.sleep(2)
            self.lp.setPassword(self.password)
            time.sleep(2)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            print(act_title)
            exp_title = "Dashboard / nopCommerce administration"
            print(exp_title)
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.lp.clickLogout()
                    time.sleep(5)
