def graph_as_tree(g, root): # O(n)
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

# Given a tree, its parent pointers, its root, and its nodes, return a
# dictionary mapping node -> sizes of its subtree.
#
# Optional node_weights arg allows specification of weight for each node.
# Otherwise, each node is assumed to have a weight of 1.
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

