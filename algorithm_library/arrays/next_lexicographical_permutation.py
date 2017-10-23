# Next lexicographical permutation
#
# Computes the next lexicographical permutation of the specified list in place,
# returning whether a next permutation existed. (Returns False when the argument
# is already the last possible permutation.)
#
# Example:
#   arr = [0, 1, 0]
#   next_permutation(arr)  (returns True)
#   arr has been modified to be [1, 0, 0]
#
# Credit: Project Nayuki
# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
def next_permutation(xs):
    n = len(xs)
    idx = n-1
    while idx > 0 and xs[idx-1] >= xs[idx]:
        idx -= 1
    if idx <= 0:
        return False
    
    j = n-1
    while xs[j] <= xs[idx-1]:
        j -= 1
    xs[idx-1], xs[j] = xs[j], xs[idx-1]
    
    xs[idx:] = xs[n-1:idx-1:-1]

    return True