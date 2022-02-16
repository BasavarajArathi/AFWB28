import pytest

@pytest.fixture(params=[("Agra","Tajmahal","White"),("Beluru","Temple","Gray"),("Goa","Beach","Blue")])
def city(request):
    return request.param

def test_create_city(city):
    print("test_create_city")
    for v in city:
        print(v)

