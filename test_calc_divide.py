import pytest

from calc import divide


def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero_raises():
    with pytest.raises(ValueError):
        divide(1, 0)
