from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected

def test_fibonacci_three():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_fibonacci_four():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_three():
    actual = lucas(3)
    expected = 4
    assert actual == expected

def test_lucas_four():
    actual = lucas(4)
    expected = 7
    assert actual == expected
    
def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_sum_series_zero():
    actual = sum_series(0)
    expected = 0
    assert actual == expected

def test_sum_series_one():
    actual = sum_series(1)
    expected = 1
    assert actual == expected

def test_sum_series_lucas_five():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected

def test_sum_series_fib_five():
    actual = sum_series(5,0,1)
    expected = 5
    assert actual == expected

