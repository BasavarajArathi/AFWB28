import pytest

@pytest.fixture(params=["Apple","Berry","Chiku"])
def fruits(request):
    return request.param

def test_eat(fruits):
    print(fruits)
