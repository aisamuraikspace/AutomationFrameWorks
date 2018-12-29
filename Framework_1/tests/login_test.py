from selenium import webdriver
import pytest
import time
import unittest
import HtmlTestRunner
from Framework_1.utils import utils as utils
from Framework_1.pages.loginPage import LoginPage
from Framework_1.pages.homePage import HomePage


class TestLogin():

    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C:/Users/mlively/PycharmProjects/AutomationFrameWorks/Framework_1/drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")


    def test_login(self, test_setup):
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()
        x = driver.title
        assert x=="OrangeHRM"

    def test_logout(self, test_setup):

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        print("test completed")

