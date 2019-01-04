import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Firefox(executable_path="C:/Users/mlively/PycharmProjects/AutomationFrameWorks/Framework_2/drivers/geckodriver.exe")

@pytest.yield_fixture()
def setUp():
    print("method level setUP")
    yield
    print("method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    if browser == "firefox":
        baseURL = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox(executable_path="C:/Users/mlively/PycharmProjects/AutomationFrameWorks/Framework_2/drivers/geckodriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.get(baseURL)
        print("Running FF")
    else:
        baseURL = "https://letskodeit.teachable.com"
        driver = webdriver.Chrome(executable_path="C:/Users/mlively/PycharmProjects/AutomationFrameWorks/Framework_2/drivers/chromedriver.exe")
        driver.get(baseURL)
        print("Running Chrome")
    yield driver
    driver.quit()
    print("module 1 time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type in System")

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class")
def osType(request):
    return request.config.getoption("--osType")



