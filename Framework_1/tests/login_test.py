import allure
from selenium import webdriver
import pytest
import time
import unittest
import moment
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
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            #assert x == "OrangeHRM"
            assert x == "HRM"
            print("test completed")

        except AssertionError as error:
            print("Assertion error")
            print(error)
            currTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            realName = utils.whoami()
            screenShotName = realName + "_" + currTime

            allure.attach(self.driver.get_screenshot_as_png(), name=screenShotName,attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/mlively/PycharmProjects/AutomationFrameWorks/Framework_1/screenshots/"+screenShotName+".png")
            raise

        except:
            print("There was an exception")
            raise

        else:
            print("No Error Occured")

        finally:
            print("run code or perform task regardless of error")

