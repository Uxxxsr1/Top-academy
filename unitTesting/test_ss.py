import pytest
import main

def test_AddPositive():
    x = 4
    y = 2
    reswait = 8
    res = main.mul(x, y)
    assert res == reswait
def test_AddPositive1():
    x = 4
    y = 2
    reswait = 2
    res = main.sub(x, y)
    assert res == reswait
