import pytest


@pytest.mark.user
@pytest.mark.smoke
def test_create_user():
    print("test_create_user")


@pytest.mark.user
@pytest.mark.regression
def test_delete_user():
    print("test_delete_user")


@pytest.mark.product
@pytest.mark.smoke
def test_create_product():
    print("test_create_product")


@pytest.mark.product
@pytest.mark.regression
def test_delete_product():
    print("test_delete_product")


@pytest.mark.customer
@pytest.mark.smoke
def test_create_customer():
    print("test_create_customer")


@pytest.mark.customer
@pytest.mark.regression
def test_delete_customer():
    print("test_delete_customer")
