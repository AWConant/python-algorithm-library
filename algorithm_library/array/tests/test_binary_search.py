from .. import binary_search

import pytest

def test_general():
    assert binary_search.binary_search([3, 5, 7, 9, 78, 98, 56555], 4) == -1
    assert binary_search.binary_search([3, 5, 7, 9, 78, 98, 56555], 5) == 1
    assert binary_search.binary_search([3, 5, 7, 9, 78, 98, 56555], 56555) == 6
    assert binary_search.binary_search([3, 5, 7, 9, 78, 98, 56555], 3) == 0

def test_small():
    assert binary_search.binary_search([1], 1) == 0
    assert binary_search.binary_search([1], 0) == -1
    assert binary_search.binary_search([], 0) == -1