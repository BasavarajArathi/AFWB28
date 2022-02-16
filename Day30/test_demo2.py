import pytest
a=100
b=200
@pytest.mark.skipif(a<b,reason="a < b so skipping")
def test_create_user():
    print("Create User")
