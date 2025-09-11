from main import add, divide
import pytest
def test_add():
    assert add(2, 3) == 5,"2 + 3 should equal 5"
    assert add(-1, 1) == 0,"-1 + 1 should equal 0"
    assert add(0, 0) == 0,"0 + 0 should equal 0"

def test_divide():
    assert divide(6, 3) == 2,"6 divided by 3 should equal 2"
    assert divide(5, 2) == 2.5,"5 divided by 2 should equal 2.5"
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)  # This should raise an error for division by zero