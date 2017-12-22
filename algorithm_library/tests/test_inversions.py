from arrays.inversions import sort_count

import pytest

@pytest.mark.parametrize("xs, correct_inv_count", [
    ([2], 0),
    ([], 0),
    ([2, 4, 1, 3, 5], 3),
    ([1, 20, 6, 4], 3),
    ([1, 2, 3, 4, 5], 0),
    ([2, 1, 3, 4, 5], 1),
])
def test_general(xs, correct_inv_count):
    in_order, inv_count = sort_count(xs)
    assert in_order == sorted(xs)
    assert correct_inv_count == inv_count
