import functools
import math

def rmq_idx(left_idx, right_idx, array):
    if array[left_idx] < array[right_idx]:
        return left_idx
    else:
        return right_idx

class SparseTable(object):
    def __init__(self, array, f, use_idx):
        self.array = array
        self.f = f
        self.use_idx = use_idx

        self.size = len(array)
        self.sparse_table = self._get_sparse_table()

    def query(self, lo, hi):
        k = math.floor(self._log2(hi-lo+1))
        left = self.sparse_table[lo][k]
        right = self.sparse_table[hi+1 - self._pow2(k)][k]

        return self.f(left, right, self.array)

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
            sparse_table[i][0] = i if self.use_idx else self.array[i]

        j = 1
        while self._pow2(j) <= self.size:
            i = 0
            while i-1 + self._pow2(j) < self.size:
                left = sparse_table[i][j-1]
                right = sparse_table[i + self._pow2(j-1)][j-1]
                sparse_table[i][j] = self.f(left, right, self.array)
                i += 1
            j += 1

        return sparse_table

