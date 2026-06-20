import pytest


def calculate_discount(price, percent):
    expected = price*(1 - percent/100)
    return expected

@pytest.mark.parametrize("price,percent,expected", [
    (100, 10, 90),
    (200, 25, 150),
    (100, 0, 100),
    (100, 100, 0),
    (50, 20, 40),
])

def test_calculate_discount(price,percent,expected):
   assert calculate_discount(price, percent) == expected
    