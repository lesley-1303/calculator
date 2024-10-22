import pytest
from Calculator import Calculator

# documentation
@pytest.fixture
def calculator():
    return Calculator()


def test_summation(calculator):
    assert 10 == calculator.summation(5, 5)


def test_difference(calculator):
    assert 4 == calculator.difference(8, 4)

def test_product(calculator):
    assert 25 == calculator.product(5, 5)


def test_quotient(calculator):
    assert 2 == calculator.quotient(8, 4)