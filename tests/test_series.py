from math_series import __version__

from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


def test_fib():
    #arrange
    expected = '13'
    #assign
    actual = fibonacci(8)
    #assert
    assert expected == actual

def test_luc():
    #arrange
    expected = '7'
    #assign
    actual = lucas(5)
    #assert
    assert expected == actual


def test_sum_series_one():
    #arrange
    expected = '7'
    #assign
    actual = sum_series(5,2,1)
    #assert
    assert expected == actual


def test_sum_series_two():
    #arrange
    expected = '13'
    #assign
    actual = sum_series(8)
    #assert
    assert expected == actual

def test_sum_series_two():
    #arrange
    expected = '14'
    #assign
    actual = sum_series(4,4,5)
    #assert
    assert expected == actual