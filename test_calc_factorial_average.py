import pytest

from calc import average, factorial


def test_factorial():
    assert factorial(5) == 120

def test_factorial_negative_raises():
    with pytest.raises(ValueError):
        factorial(-1)

def test_average():
    assert average([2, 4, 6]) == 4

def test_average_empty():
    assert average([]) == 0
