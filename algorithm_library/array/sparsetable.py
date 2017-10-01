import functools
import math

def rmq_idx(left_idx, right_idx, array):
    """
    A Sparse Table constructed with this function as its function acts as a
    handler for queries requesting the index of the minimum value.
    """
    if array[left_idx] < array[right_idx]:
        return left_idx
    else:
        return right_idx

class SparseTable(object):
    """
    A data structure useful for answering range queries about a static array.
    A query is of the form (lo, hi), and requests the result of the following:

    f(a[lo], f(a[lo+1], ... f(hi-1, hi)))
    
    for some array of elements a and some binary, associative function f.
    The table is constructed in O(n*lg(n)) time and occupies the same amount of
    space. Queries are answered in constant time.
    Time complexity: 
      Construction: O(n*lg(n))
      Query: O(1)
    Space complexity: O(n*lg(n))

    array   -- an array of mutually orderable elements
    f       -- an associative, binary function
    use_idx -- boolean indicating whether table values should be initialized
               as array indices or array element values
    """
    def __init__(self, array, f, use_idx):
        self.array = array
        self.f = f
        self.use_idx = use_idx

        self.size = len(array)
        self.sparse_table = self._get_sparse_table()

    def query(self, lo, hi):
        """
        Computes and returns the value of f over the subarray array[lo:hi]
        inclusive.
        Time complexity: O(1)
        Space complexity: O(1)

        Parameters:
        lo -- the beginning index of the subarray
        hi -- the ending index of the subarray

        Returns:
        f(left, right) -- the function value over the subarray
        """
        k = math.floor(self._log2(hi-lo+1))
        left = self.sparse_table[lo][k]
        right = self.sparse_table[hi+1 - self._pow2(k)][k]

        return self.f(left, right, self.array)

    @staticmethod
    @functools.lru_cache(maxsize=None)
    def _pow2(number): # guarantees O(1) amortized time spent on powers of 2
        return 2**number

    @staticmethod
    @functools.lru_cache(maxsize=None)
    def _log2(number): # guarantees O(1) amortized time spent on logs
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

