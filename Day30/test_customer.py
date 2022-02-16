import pytest


@pytest.mark.dependency(name="create")
def test_create_customer():
    print("test_create_customer")
    assert False

@pytest.mark.dependency(depends=["create"])
def test_delete_customer():
    print("test_delete_customer")