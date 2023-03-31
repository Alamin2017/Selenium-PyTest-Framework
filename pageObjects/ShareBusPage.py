import time
from selenium.webdriver.common.by import By


class ShareBusPage:
    def __init__(self, driver):
        self.driver = driver

    def ClickSignInButton(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()
        time.sleep(3)

    def enterEmail(self, username):
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(username)

    def enterPass(self, password):
        self.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)

    def clickLoginInButton(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
