import pytest

#can we run a method automatically before every test method? Yes- using fixture
#how to use fixture?
#. create a precondition method which is to be execute before the test, using @pytest.fixture
#. specify the name of fixture method as argument in test method

@pytest.fixture
def precondition():
    print("\nopen the browser and enter url")
    print("login to the app")

def test_create_customer(precondition):
    print("create customer")


def test_create_product(precondition):
    print("create product")