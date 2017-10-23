from arrays.binary_search import binary_search

import pytest

@pytest.mark.parametrize("xs,x,idx", [
    ([3, 5, 7, 9, 78, 98, 56555], 4, -1),
    ([3, 5, 7, 9, 78, 98, 56555], 5, 1),
    ([3, 5, 7, 9, 78, 98, 56555], 56555, 6),
    ([3, 5, 7, 9, 78, 98, 56555], 3, 0),
    ([1], 1, 0),
    ([1], 0, -1),
    ([], 0, -1),
])
def test_general(xs, x, idx):
    assert binary_search(xs, x) == idx