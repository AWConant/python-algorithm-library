from .. import count_inversions

import pytest

def _test_sort_count(ls, correct_inv_count):
    in_order, inv_count = count_inversions.sort_count(ls)
    assert in_order == sorted(ls)
    assert correct_inv_count == inv_count

def test_general():
    _test_sort_count([2, 4, 1, 3, 5], 3)
    _test_sort_count([1, 20, 6, 4], 3)
    _test_sort_count([1, 2, 3, 4, 5], 0)
    _test_sort_count([2, 1, 3, 4, 5], 1)

def test_small():
    _test_sort_count([2], 0)
    _test_sort_count([], 0)