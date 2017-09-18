def get_subtree_sizes(tree, parent_of, root, nodes, node_weights=None):
    """
    Deduce the size of each subtree rooted at each node.
    Time complexity: O(V)
    Space complexity: O(V)

    Parameters:
    tree         -- dictionary mapping node label to adjacent nodes. represents
                    directed tree with root as the root node (only node with no
                    incoming edges)
    parent_of    -- dictionary mapping node label to the label of its parent. the
                    parent of the root is None.
    root         -- label of node to be considered the root of the tree
    nodes        -- iterable over names of all nodes in g
    node_weights -- (optional) dictionary mapping node labels to their respective
                    weights. if unspecified, node weights are 1.

    Returns:
    subtree_sizes -- dictionary mapping node label to the size of the subtree
                     rooted there.
    """
    if node_weights is not None:
        subtree_sizes = dict(node_weights)
    else:
        subtree_sizes = {node: 1 for node in nodes}

    visited = set()
    stack = [root]
    while stack:
        node = stack.pop()

        for child in tree[node]:
            if child not in visited:
                visited.add(child)
                stack.append(child)
                break
        else:
            if node != root:
                subtree_sizes[parent_of[node]] += subtree_sizes[node]
                stack.append(parent_of[node])

    return subtree_sizes
