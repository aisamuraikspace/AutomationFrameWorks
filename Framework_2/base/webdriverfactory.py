from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser

    def getWebDriverInstance(self):

        baseURL = "https://letskodeit.teachable.com"

        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()

        driver.implicity_wait(3)

        driver.maximize_window()

        driver.get(baseURL)

        return driver



