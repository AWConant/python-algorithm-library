from arrays.kadanes import kadanes

import pytest

@pytest.mark.parametrize('array,expected', [
    ([], 0),
    ([0], 0),
    ([1], 1),
    ([-1], 0),
    ([-2, -3, 4, -1, -2, 1, 5, -3], 7),
])
def test_general(array, expected):
    assert kadanes(array) == expected
