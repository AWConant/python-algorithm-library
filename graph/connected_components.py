# Connected components in _undirected_ graph
def connected_components(g, nodes): # O(V+E)
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
    return [dfs_get_component(node, visited) for node in nodes if node not in visited]]
