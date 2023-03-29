from utilities.readProperties import ReadConfig
import time

class Test_ShareBus:

    baseURL = ReadConfig.getApplicationURLBkash()
    def test_urlopen(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        time.sleep(3)
