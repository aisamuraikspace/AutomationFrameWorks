import pytest

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Firefox(executable_path="C:/Users/mlively/PycharmProjects/AutomationFrameWorks/Framework_2/drivers/geckodriver.exe")

@pytest.yield_fixture()
def setUp():
    print("method level setUP")
    yield
    print("method level tearDown")

@pytest.yield_fixture(scope="module")
def oneTimeSetUp(browser, osType):
    print("module 1 time setUP")
    if browser == "firefox":
        print("Running FF")
    else:
        print("Running Chrome")
    yield
    print("module 1 time tearDown")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")