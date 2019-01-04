import pytest
from selenium import webdriver
from Framework_2.base.webdriverfactory import WebDriverFactory


@pytest.fixture(scope="class")
def test_setup(request):
    driver = webdriver.Firefox()

@pytest.yield_fixture()
def setUp():
    print("method level setUP")
    yield
    print("method level tearDown")

@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("one time setup")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    if request.cls is not None:
        request.cls.driver = driver
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



