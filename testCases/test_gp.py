from utilities.readProperties import ReadConfig
import time


class Test_MY_GP:
    baseURL2 = ReadConfig.getApplicationURL2()

    def test_just(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL2)
        time.sleep(5)
