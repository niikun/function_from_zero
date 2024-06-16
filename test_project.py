from mylib.calc import add, sub, mul, div
import pytest


#write test for each function in calc.py

def test_add():
    assert add(2, 3) == 5
    assert add(2, -3) == -1
    assert add(2, 0) == 2
    assert add(0, 0) == 0

def test_sub():
    assert sub(2, 3) == -1
    assert sub(2, -3) == 5
    assert sub(2, 0) == 2
    assert sub(0, 0) == 0

def test_mul():
    assert mul(2, 3) == 6
    assert mul(2, -3) == -6
    assert mul(2, 0) == 0
    assert mul(0, 0) == 0

def test_div():
    assert div(2, 3) == 2/3
    assert div(2, -3) == 2/-3
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        div(2, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        div(0, 0)

