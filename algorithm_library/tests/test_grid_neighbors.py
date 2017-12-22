from graph.grid_neighbors import iterate_neighbors

import pytest

@pytest.mark.parametrize('r,c,r_max,c_max,expected,length', [
    (0, 0, 5, 5, {(1, 0), (0, 1), (1, 1)}, 3),
    (1, 1, 5, 5, {(1, 0), (0, 1), (0, 0), (2, 2), (2, 1), (1, 2), (2, 0), (0, 2)}, 8),
])
def test_general(r, c, r_max, c_max, expected, length):
    neighbors = list(iterate_neighbors(r, c, r_max, c_max))
    assert length == len(neighbors)
    assert expected == set(neighbors)