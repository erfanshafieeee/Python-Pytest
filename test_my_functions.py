import pytest

import my_funtions as my_func
import time


def test_add():
    result = my_func.add(1,4)
    assert result ==5
# should be pass

def test_add_strings():
    res = my_func.add("i like ","pizza")
    assert res =="i like pizza"

# should be pass

def test_divide():
    res = my_func.divide(10 ,5)
    assert res ==2

#should be pass

@pytest.mark.xfail(reason="We know that divide by zero is not supported")
def test_divide_by_zero_1():
    res = my_func.divide(10,0)
    assert res == 2

#should be fail


def test_divide_by_zero_2():
    with pytest.raises(ZeroDivisionError):
        my_func.divide(10,0)

#should be pass


@pytest.mark.skip(reason="this feature is currently broken")
def test_add():
    assert my_func.add(1 , 2)==3

@pytest.mark.slow
def test_add_slowly():
    time.sleep(5)
    assert my_func.add(1 , 2)==3





