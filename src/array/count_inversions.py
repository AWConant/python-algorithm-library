def sort_count(ls):
    """
    Counts the inversions in an list while building a sorted copy.

    Parameters:
    ls -- a list of orderable values

    Returns:
    M         -- a sorted copy of the input list
    inv_count -- total number of inversions in list
    """

    if len(ls) < 2:
        return ls, 0

    mid_idx = len(ls)//2
    first_half, first_half_inv_count = sort_count(ls[:mid_idx])
    second_half, second_half_inv_count = sort_count(ls[mid_idx:])

    combine_inv_count = 0
    i = j = 0
    sorted_list = []

    # cuts down on time spent in tight loop.
    sorted_list_append = sorted_list.append
    first_length, second_length = len(first_half), len(second_half)

    while i < first_length and j < second_length:
        if first_half[i] <= second_half[j]:
            sorted_list_append(first_half[i])
            i += 1
        else:
            combine_inv_count += first_length - i
            sorted_list_append(second_half[j])
            j += 1

    inv_count = first_half_inv_count + second_half_inv_count + combine_inv_count

    sorted_list.extend(first_half[i:])
    sorted_list.extend(second_half[j:])

    return sorted_list, inv_count
