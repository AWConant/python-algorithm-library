from datastructures.unionfind import UnionFind

import pytest
import itertools

def test_general():
    uf = UnionFind(list(range(10)))

    assert uf.same_set(0, 0)
    assert not uf.same_set(0, 1)

    uf.union(0, 1)

    assert uf.same_set(0, 1)
    assert not uf.same_set(0, 2)
    assert not uf.same_set(1, 2)

    uf.union(1, 2)

    assert uf.same_set(0, 2)
    assert not uf.same_set(8, 9)
    assert not uf.same_set(0, 9)
    assert not uf.same_set(1, 9)
    assert not uf.same_set(2, 9)

    # merge all sets
    for key2 in range(3, 10):
        uf.union(0, key2)

    for key1, key2 in itertools.product(range(10), range(10)):
        assert uf.same_set(key1, key2)
