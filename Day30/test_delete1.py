import pytest

@pytest.mark.run(order=6)
def test_delete_customer():
    print("test_delete_customer")


@pytest.mark.run(order=2)
def test_delete_user():
    print("test_delete_user")

@pytest.mark.run(order=4)
def test_delete_product():
    print("test_delete_product")


