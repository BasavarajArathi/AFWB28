import pytest

@pytest.mark.run(order=5)
def test_create_customer():
 print("test_create_customer")

@pytest.mark.run(order=1)
def test_create_user():
  print("test_create_user")

@pytest.mark.run(order=3)
def test_create_product():
   print("test_create_product")



