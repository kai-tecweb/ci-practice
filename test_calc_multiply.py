from calc import multiply


def test_multiply():
    assert multiply(4, 3) == 12

def test_multiply_by_zero():
    assert multiply(4, 0) == 0
