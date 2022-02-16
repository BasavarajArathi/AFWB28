import pytest

@pytest.mark.run(order=1)
def test_create_user():
  print("test_create_user")

@pytest.mark.run(order=2)
def test_create_product():
   print("test_create_product")



