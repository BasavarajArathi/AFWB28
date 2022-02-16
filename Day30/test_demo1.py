import pytest


class Test_Demo1:
    def test_login(self):
        print("m1")

    def test_create_user(self):
        print("m2")

    @pytest.mark.skip
    def test_delete_user(self):
        print("m3")