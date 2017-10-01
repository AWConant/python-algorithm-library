from .. import lca

import pytest
from collections import defaultdict

@pytest.mark.parametrize('edges,queries,expected', [
    (
        [(1, 2), (1, 3), (2, 4), (2, 5), (2, 6), (3, 7), (3, 8)],
        [(6, 7), (6, 4)],
        [1, 2]
        ),
])
def test_general(edges, queries, expected):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    lca_handler = lca.LCAStaticTree(graph, 1)
    for query, correct in zip(queries, expected):
        assert lca_handler.query(*query) == correct