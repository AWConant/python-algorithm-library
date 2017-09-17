# Obtain directed tree, parent pointers, and a list of leaves from undirected
# graph.  Input graph must be undirected and have n-1 edges (must be a tree).
#
# Returns tree as adjacency list, parent pointers as dictionary, and a list of
# leaves.
# The parent of the root is None.
def graph_as_tree(g, root): # O(n)
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

# BFS a tree from leaves->root given its child pointers.
def bfs_tree_from_leaves(children, root):
    from collections import deque

    stack = deque()
    q = deque([root])
    while q:
        node = q.popleft()
        q.extend(children[node])
        stack.appendleft(node)

    yield from stack

