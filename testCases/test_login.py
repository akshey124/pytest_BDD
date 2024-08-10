import time

# import pytest
# from selenium import webdriver
from pageObjects.Loginpage import LoginPage
from testCases.confitest import setup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("********************** Test_001_Login **********************")
        self.logger.info("********************** Verifying Home Page Title **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:\\Users\\akshe\\PycharmProjects\\Hybridframework\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        actual_title = self.driver.title
        time.sleep(5)

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:\\Users\\akshe\\PycharmProjects\\Hybridframework\\Screenshots\\test_login.png")
            self.driver.close()
            assert False
