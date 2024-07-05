import pytest
from arithmetic import add, subtract, multiply, divide

def test_add():
    """Test the add function."""
    assert add(1, 2) == 3

def test_subtract():
    """Test the subtract function."""
    assert subtract(2, 1) == 1

def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6

def test_divide():
    """Test the divide function."""
    assert divide(6, 2) == 3

def test_divide_by_zero():
    """Test divide by zero raises ValueError."""
    with pytest.raises(ValueError):
        divide(1, 0)
