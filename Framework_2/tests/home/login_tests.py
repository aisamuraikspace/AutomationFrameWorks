from selenium import webdriver
from selenium.webdriver.common.by import By
from Framework_2.pages.home.login_page import LoginPage
import unittest

driver = webdriver.Firefox(executable_path="C:/Users/mlively/PycharmProjects/AutomationFrameWorks/Framework_2/drivers/geckodriver.exe")


class LoginTests(unittest.TestCase):

    def test_validLogin(self):
        baseURL="https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)

        lp=LoginPage(driver)
        lp.login("test@email.com", "abcabc")

        userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='Test User']")

        if userIcon is not None:
            print("Login Successful")
        else:
            print("Login Failed")

