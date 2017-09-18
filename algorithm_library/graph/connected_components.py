def connected_components(g, nodes):
    """
    Partitions the nodes of an undirected graph into connected components.
    Time complexity: O(V+E)
    Space complexity: O(V)

    Parameters:
    g     -- graph as an adjacency list (dictionary mapping node label to
             list of adjacent nodes)
    nodes -- iterable over names of all nodes in g

    Returns:
    a list of lists, where each sublist contains nodes that are in the same
    connected component in g.
    """
    def dfs_get_component(start, visited):
        component = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                component.append(node)
                stack.extend(g[node])
        return component

    visited = set()
    return [dfs_get_component(node, visited) for node in nodes if node not in visited]
