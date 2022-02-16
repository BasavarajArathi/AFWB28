import pytest

#How do we compare 2 values in pyTest -- verification

def test_login():
    print("open the browser")
    print("enter the URL")
    print("enter valid un & pwd")
    print("click login button")
    print("Verify that home page displayed")
    eTitle="Home Page"
    aTitle="Home Page2"
    assert aTitle == eTitle
