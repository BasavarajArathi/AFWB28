import pytest

#can we run a method automatically before every test method? Yes- using fixture
#how to use fixture?
#. create a precondition method which is to be execute before the test, using @pytest.fixture
#. specify the name of fixture method using @pytest.mark.usefixtures

@pytest.fixture
def precondition():
    print("\nopen the browser and enter url")
    print("login to the app")

@pytest.mark.usefixtures("precondition")
def test_create_customer():
    print("create customer")

@pytest.mark.usefixtures("precondition")
def test_create_product():
    print("create product")