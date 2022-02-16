import pytest

@pytest.fixture(params=["Agra","Beluru","Chennai"])
def city(request):
    return request.param


def test_create_city(city):
    print("test_create_city")
    print(city)

def test_edit_city(city):
    print("test_edit_city")
    print(city)
