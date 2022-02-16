import pytest


@pytest.mark.parametrize("fn",["Bhanu","Ravi","Surya"])
def test_customer(fn):
    print("create customer:",fn)

