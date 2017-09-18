def reverse_linked_list(xs):
    """
    Reverse a singly-linked list in place.
    Time complexity: O(n)
    Space complexity: O(1)

    Parameters:
    xs -- a singly-linked list

    Returns:
    new -- a reference to the head of the reversed list
    """
    new = None
    while xs:
        xs.next, xs, new = new, xs.next, xs
    return new
