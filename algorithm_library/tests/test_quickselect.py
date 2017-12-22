from arrays.quickselect import quickselect

import pytest

@pytest.mark.parametrize("xs,k,expected", [
    ([2, 1, 4, 3], 0, 1),
    ([1, 2, 5, 4, 3], 0, 1),
    ([3, 4, 1, 2, 5], 4, 5),
    ([], 4, None),
])
def test_general(xs, k, expected):
    assert quickselect(xs, k) == expected

def test_exception():
    with pytest.raises(IndexError):
        quickselect([1,2,3], 6)
        quickselect([1,2,3], -1)