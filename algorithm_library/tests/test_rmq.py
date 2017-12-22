from datastructures.sparsetable import SparseTable, rmq_idx

import pytest

@pytest.mark.parametrize('array,queries,expected', [
    (
        [7, 2, 3, 0, 5, 10, 3, 12, 18],
        [(1, 1), (0, 4), (4, 7), (7, 8)],
        [1, 3, 6, 7],
    ),
])
def test_general(array, queries, expected):
    rmq_handler = SparseTable(array, rmq_idx, True)
    for query, correct in zip(queries, expected):
        assert rmq_handler.query(*query) == correct
