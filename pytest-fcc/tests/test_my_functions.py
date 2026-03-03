import pytest
import time
import source.my_functions as my_functions


def test_add():
    result = my_functions.add(1, 4)
    assert result == 5


def test_divide():
    result = my_functions.divide(10, 5)
    assert result == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)
    assert True

@pytest.mark.slow # Useful to use when you have a test that takes a long time to run, and you want to be able to easily skip it when running your tests.
def test_very_slow_test():
    time.sleep(5)
    result = my_functions.divide(10, 5)
    assert result == 2


@pytest.mark.skip(reason="This feature is broken") # Useful to use when you have a test that is not ready yet, and you want to be able to easily skip it when running your tests.
def test_add():
    assert my_functions.add(1, 4) == 5


@pytest.mark.xfail(reason="We know we cannot divide by zero")
# Useful to use when you have a test that is expected to fail, and you want to be able to easily mark it as such when running your tests.
def test_divide_by_zero():
    my_functions.divide(10, 0)
