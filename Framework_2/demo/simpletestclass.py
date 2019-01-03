import pytest

@pytest.mark.usefixture("coreTimeSetUp", "setUp")
class TestClassDemo():

    def test_methodA(self):
        print("A")

    def test_methodB(self):
        print("B")