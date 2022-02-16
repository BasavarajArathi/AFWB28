import pytest
#to reuse a fixture in multiple .py files , mention the fixture method in conftest.py
@pytest.fixture(autouse=True)
def fruits():
   print("wash fruit")