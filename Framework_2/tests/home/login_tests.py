from selenium import webdriver
from Framework_2.pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("text@email.com", "abcabc")
        result1 = self.lp.verifyTitle()
        assert result1 == True
        result2 = self.lp.verifyLoginSuccessful()
        assert result2 == True


    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabcasdf")
        result = self.lp.verifyLoginFailed()
        assert result == True


