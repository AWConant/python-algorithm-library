import functools
import math

class RMQStaticArray(object):
    def __init__(self, array):
        self.array = array
        self.size = len(array)
        self.sparse_table = self._get_sparse_table()

    def query(self, lo, hi):
        split_idx = math.floor(self._log2(hi-lo+1))
        lo_min_idx = self.sparse_table[lo][split_idx]
        hi_min_idx = self.sparse_table[hi+1 - self._pow2(split_idx)][split_idx]

        return min(lo_min_idx, hi_min_idx, key=lambda idx: self.array[idx])

    @staticmethod
    @functools.lru_cache(maxsize=None)
    def _pow2(number):
        return 2**number

    @staticmethod
    @functools.lru_cache(maxsize=None)
    def _log2(number):
        return math.log2(number)

    def _get_sparse_table(self):
        subarray_size = math.ceil(self._log2(self.size))
        sparse_table = [[None for _ in range(subarray_size)] for _ in range(self.size)]

        for i in range(self.size):
            sparse_table[i][0] = i

        j = 1
        while self._pow2(j) <= self.size:
            i = 0
            while i-1 + self._pow2(j) < self.size:
                lo_min_idx = sparse_table[i][j-1]
                hi_min_idx = sparse_table[i + self._pow2(j-1)][j-1]
                sparse_table[i][j] = min(lo_min_idx, hi_min_idx, key=lambda idx: self.array[idx])
                i += 1
            j += 1

        return sparse_table

