from example import add, subtract
import pytest


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'




# uncomment the following test in step 5
#def test_subtract():
#    assert subtract(2, 3) == -1
