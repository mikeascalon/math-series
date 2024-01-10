from math_series.series import fibonacci, lucas

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
    actual = fibonacci(3)
    expected = 2
    assert actual == expected

def test_lucas_zero():
    actual = lucas(0)
    expect = 2

def test_lucas_one():
    actual = lucas(1)
    expect = 1

def test_lucas_three():
    actual = lucas(3)
    expect = 3

def test_lucas_four():
    actual = lucas(4)
    expect = 4
    
def test_lucas_five():
    actual = lucas(5)
    expect = 7