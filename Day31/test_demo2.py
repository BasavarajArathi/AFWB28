import pytest
#to run a test multiple times with diff inputs we should use 'parameterize'


@pytest.mark.parametrize("customer_name",("bhanu","basava"))
def test_customer(customer_name):
        print("create customer:",customer_name)

@pytest.mark.parametrize("name,mrp",[("java",10000),("selenium",12000)])
def test_product(name,mrp):
        print("product name:",name)
        print("product mrp:", mrp)
