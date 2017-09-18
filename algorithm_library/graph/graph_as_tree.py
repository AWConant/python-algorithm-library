def graph_as_tree(g, root):
    """
    Obtain a directed tree, parent pointers, and a list of leaves from an
    undirected graph.
    Time complexity: O(V)
    Space complexity: O(V)

    Parameters:
    g    -- graph as an adjacency list (dictionary mapping node label to
            list of adjacent nodes). graph must be undirected and must
            have V-1 edges.
    root -- label of node to be considered the root of the tree

    Returns:
    tree      -- dictionary mapping node label to adjacent nodes. represents
                 directed tree with root as the root node (only node with no
                 incoming edges)
    parent_of -- dictionary mapping node label to the label of its parent. the
                 parent of the root is None.
    leaves    -- list of nodes that are leaves of the tree (nodes with no outgoing
                 edges)
    """
    from collections import defaultdict

    tree = defaultdict(list)
    parent_of = dict()
    leaves = list()

    stack = [(root, None)]
    while stack:
        node, prev = stack.pop()

        parent_of[node] = prev

        children = [v for v in g[node] if v != prev]
        if len(children) == 0:
            leaves.append(node)
        else:
            tree[node].extend(children)
            for child in children:
                stack.append( (child, node) )

    return tree, parent_of, leaves
