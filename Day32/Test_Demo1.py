import pytest


@pytest.mark.parametrize("city",["Agra","Beluru","Chennai"])
def test_create_city(city):
    print(city)

@pytest.mark.parametrize("city",["Agra","Beluru","Chennai"])
def test_edit_city(city):
    print(city)

@pytest.mark.parametrize("city",["Agra","Beluru","Chennai"])
def test_delete_city(city):
    print(city)
