import pytest

from utils.arrs import get


def test_get():
    assert get([1, 2, 3], 1, "test") == 2
