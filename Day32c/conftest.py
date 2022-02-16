import pytest
#to reuse a fixture in multiple .py files , mention the fixture method in conftest.py
#scope:
#--> function----> run this fixture method automatically for every test method (funtion)
# @pytest.fixture(scope="function",autouse=True)
# def login_and_logout():
#    print("\nlogin to application")
#    yield
#    print("\nlogout to application")

#--> class----> run this fixture method automatically for every class
# @pytest.fixture(scope="class",autouse=True)
# def login_and_logout():
#    print("\nlogin to application")
#    yield
#    print("\nlogout to application")

#--> module----> run this fixture method automatically for every file (module)

# @pytest.fixture(scope="module",autouse=True)
# def login_and_logout():
#    print("\n***login to application***")
#    yield
#    print("\n***logout to application***")


# @pytest.fixture(scope="package",autouse=True)
# def login_and_logout():
#    print("\n***login to application***")
#    yield
#    print("\n***logout to application***")

@pytest.fixture(scope="session",autouse=True)
def login_and_logout():
   print("\n***login to application***")
   yield
   print("\n***logout to application***")
