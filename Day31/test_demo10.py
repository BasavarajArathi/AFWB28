import pytest

#can we run a method automatically before every test method? Yes- using fixture
#how to use fixture?
#. create a precondition method which is to be execute before the test, using @pytest.fixture with autouse


@pytest.fixture(autouse=True)
def precondition():
    print("\nopen the browser and enter url")
    print("login to the app")


def test_create_customer():
    print("create customer")


def test_create_product():
    print("create product")