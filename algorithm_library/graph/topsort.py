def topsort(g, nodes):
    """
    An implementation of Kahn's algorithm.
    Returns a topological ordering of an input DAG.
    Time complexity: O(V+E)
    Space complexity: O(V)

    Parameters:
    g     -- graph as an adjacency list (dictionary mapping node label to
             list of adjacent nodes)
    nodes -- iterable containing each node label

    Returns:
    topological_ordering -- list containing a topologically-sorted ordering
        of the input graph's nodes.

    Credit:
    Inspired from geeksforgeeks (Chirag Agarwal)
    http://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
    """
    from collections import deque

    in_degree = {node: 0 for node in nodes}

    for neighbors in g.values():
        for neighbor in neighbors:
            in_degree[neighbor] += 1

    q = deque([node for node in nodes if in_degree[node] == 0])
    top_order = []

    while q:
        node = q.popleft()
        top_order.append(node)

        for neighbor in g[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    return top_order
