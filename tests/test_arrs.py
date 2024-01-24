import pytest

from utils.arrs import get, my_slice


def test_get():
    assert get([1, 2, 3], 1, "test") == 2
    assert get([1, 2, 3, 4, 5], 3, "test") == 4
    assert get([1, 2, 3, 4, 5, 6], -1, "test")

def test_my_slice():
    assert my_slice([1, 2, 3, 4, 5], 2, -1) == [3, 4]
    assert my_slice([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]
    assert my_slice([1, 2, 3, 4, 5], 1, 5) == [2, 3, 4, 5]
