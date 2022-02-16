import pytest

@pytest.mark.dependency(name="create_customer")
def test_create_customer():
    print("test_create_customer")
    # assert False

@pytest.mark.dependency(depends=["create_customer"])
def test_delete_customer():
    print("test_delete_customer")