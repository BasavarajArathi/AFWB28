import pytest


@pytest.fixture(autouse=True)
def precondition():
    print("open the application")
    yield
    print("close the application")


def test_create_customer():
    print("create customer")


def test_create_product():
    print("create product")
