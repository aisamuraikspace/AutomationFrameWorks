from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver

    def getByType9(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By. CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType = "id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element Found")
        except:
            print("Element not Found")
            return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            print("Click on element " + locator + " type "+locatorType)
        except:
            print("Can not click on element " + locator + " type " + locatorType)
            print_stack()

    def sendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print("Send Data on element " + locator + " type "+locatorType)
        except:
            print("Can not Send Data on element " + locator + " type " + locatorType)
            print_stack()

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                print("Element Found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            print("Waiting for maximum:: " + str(timeout)+ " :: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
                                                                                        ElementNotVisibleException,
                                                                                        ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, "stop filter stops")))
            print("Element on web page")
        except:
            print("Element not on web page")
            print_stack()
        return element



