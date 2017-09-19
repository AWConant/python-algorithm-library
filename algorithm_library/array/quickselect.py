def quickselect(xs, k):
    """
    Find k'th smallest element in an array.
    Time complexity: O(n)
    Space complexity: O(lg(n))

    Parameters:
    xs --
    lo --
    hi --
    k  --
    ...

    Returns:
    x    -- k'th smallest element in xs
    None -- if empty list is passed

    Raises:
    IndexError -- if invalid k is passed

    Credit:
    KoderDojo
    http://www.koderdojo.com/blog/quickselect-algorithm-in-python
    """
    from random import randint

    def select(xs, lo, hi, k):
        if hi == lo:
            return xs[lo]

        pidx = randint(lo, hi)

        xs[lo], xs[pidx] = xs[pidx], xs[lo]

        i = lo
        for j in range(lo+1, hi+1):
            if xs[j] < xs[lo]:
                i += 1
                xs[i], xs[j] = xs[j], xs[i]

        xs[i], xs[lo] = xs[lo], xs[i]

        if k == i:
            return xs[i]
        elif k < i:
            return select(xs, lo, i-1, k)
        else:
            return select(xs, i+1, hi, k)

    if len(xs) == 0:
        return None

    if k < 0 or k > len(xs) - 1:
        raise IndexError

    return select(xs, 0, len(xs) - 1, k)
