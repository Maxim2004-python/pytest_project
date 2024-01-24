import pytest

from utils.arrs import get, my_slice


def test_get():
    assert get([1, 2, 3], 1, "test") == 2

def test_my_slice():
    assert my_slice([1, 2, 3, 4, 5], 2, -1) == [3, 4]
