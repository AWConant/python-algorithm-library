def binary_search(xs, x):
    """
    Binary search a sorted list for value x.
    Runs in O(lg(n)) time.

    Parameters:
    xs -- a list of orderable values sorted in nondecreasing order
    x  -- a value to search xs for
    lo -- (optional) the lowest

    Returns:
    idx -- the leftmost index of x in xs (or -1, if x is not in xs)

    Credit:
    Credit person/website
    URL
    """
    from bisect import bisect_left

    idx = bisect_left(xs, x, 0, len(xs)) 
    if idx != len(xs) and xs[idx] == x:
        return idx
    else:
        return -1
