def bfs_tree_from_leaves(tree, root):
    """
    Iterate over the nodes of a tree in reverse BFS order.
    Time complexity: O(V)
    Space complexity: O(V)

    Parameters:
    tree -- dictionary mapping node label to adjacent nodes. represents
            directed tree with root as the root node (only node with no
            incoming edges)
    root -- label of node to be considered the root of the tree

    Yields:
    nodes accumulated from BFS.
    """
    from collections import deque

    stack = deque()
    q = deque([root])
    while q:
        node = q.popleft()
        q.extend(tree[node])
        stack.appendleft(node)

    yield from stack

