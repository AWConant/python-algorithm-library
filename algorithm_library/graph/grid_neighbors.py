def iterate_neighbors(r, c, r_max, c_max):
    """
    Yields the in-bounds neighbors of a particular position in a grid.
    Time complexity: O(1)
    Space complexity: O(1)

    Parameters:
    r     -- row value of position in grid
    c     -- column value of position in grid
    r_max -- number of rows in grid
    c_max -- number of columns in grid

    Yields:
    (r_neighbor, c_neighbor) -- all neighbors that are in-bounds
    """
    if r+1 < r_max:
        yield (r+1, c)
        if c+1 < c_max:
            yield (r+1, c+1)
        if c-1 >= 0:
            yield (r+1, c-1)
    if r-1 >= 0:
        yield (r-1, c)
        if c+1 < c_max:
            yield (r-1, c+1)
        if c-1 >= 0:
            yield (r-1, c-1)
    if c+1 < c_max:
        yield (r, c+1)
    if c-1 >= 0:
        yield (r, c-1)
    