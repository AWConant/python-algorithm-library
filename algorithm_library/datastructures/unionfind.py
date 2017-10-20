class UnionFind(object):
    """
    Provides a model for disjoint sets. Initialized with n sets containing a
    single key each, UnionFind can efficiently determine whether two keys are
    in the same set as well as efficiently merge two sets.

    Time complexity: O(n)
    Space complexity: O(n)

    Parameters:
    keys -- (optional) iterable containing labels of keys known ahead of time
    """
    def __init__(self, keys=[]):
        self.parent_of = dict()
        self.rank_of = dict()

        for key in keys:
            self.make_set(key)

    def _find(self, key):
        """
        Return the root of the tree representing the set containing key.
        Connect this discovered root as the parent of key to compress the
        search path for future invocations of _find.

        Time complexity: O(a(n)) (inverse Ackerman function; basically constant)
        Space complexity: O(1)

        Parameters:
        key -- label of key
        """
        current = key

        # seek root of tree
        while self.parent_of[current] != current:
            current = self.parent_of[current]
        
        self.parent_of[key] = current # compress path

        return current

    def make_set(self, key):
        """
        Add a set containing only key to the data structure.

        Time complexity -- O(1)
        Space complexity -- O(1)

        Parameters:
        key -- label of key
        """
        self.parent_of[key] = key
        self.rank_of[key] = 1

    def union(self, key1, key2):
        """
        If key1 and key2 are in different sets, merge their sets.

        Time complexity: O(a(n)) (inverse Ackerman function; basically constant)
        Space complexity: O(1)

        Parameters:
        key1 -- label of first key
        key2 -- label of second key
        """
        root1 = self._find(key1)
        root2 = self._find(key2)

        if root1 != root2:
            if self.rank_of[root1] >= self.rank_of[root2]:
                self.rank_of[root1] += self.rank_of[root2]
                self.parent_of[root2] = root1
            else:
                self.rank_of[root2] += self.rank_of[root1]
                self.parent_of[root1] = root2

    def same_set(self, key1, key2):
        """
        If key1 and key2 are in the same set, return True. Otherwise,
        return False.

        Time complexity: O(a(n)) (inverse Ackerman function; basically constant)
        Space complexity: O(1)

        Parameters:
        key1 -- label of first key
        key2 -- label of second key
        """
        return self._find(key1) == self._find(key2)