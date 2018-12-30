from selenium import webdriver
import pytest
import time
import unittest
import HtmlTestRunner
from Framework_1.utils import utils as utils
from Framework_1.pages.loginPage import LoginPage
from Framework_1.pages.homePage import HomePage

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()
        x = driver.title
        assert x=="OrangeHRM"

    def test_logout(self):
        driver = self.driver

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        print("test completed")

