import pytest

@pytest.yield_fixture()
def setUp():
    print("method level setUP")
    yield
    print("method level tearDown")


@pytest.yield_fixture(scope="module")
def oneTimeSetUp():
    print("module 1 time setUP")
    yield
    print("module 1 time tearDown")
