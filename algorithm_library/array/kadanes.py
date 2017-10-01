def kadanes(array):
    """
    Computes the maximum among all sums of subarrays. The maximum subarray sum
    of an empty array or entirely negative array is 0.

    Time complexity: O(n)
    Space complexity: O(1)

    Parameters:
    array -- an array of numerically-typed values

    Returns:
    best_sum -- the maximum sum
    """
    best_sum = 0

    current_sum = 0
    for num in array:
        current_sum += num
        best_sum = max(current_sum, best_sum)
        current_sum = max(current_sum, 0)

    return best_sum