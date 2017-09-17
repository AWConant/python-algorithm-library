def dag_dijkstra(g, nodes, weights, start, topsort):
    """
    Get distances from a start node to each node in the input DAG.
    Runs in O(V+E) time.

    Parameters:
    g       -- graph as an adjacency list (dictionary mapping node label to
               list of adjacent nodes)
    nodes   -- iterable containing each node label
    weights -- nested dictionary containing weight of each directed edge (type:
               defaultdict(dict))
    start   -- label of origin node
    topsort -- a function that returns a topological ordering of the input DAG

    Returns:
    dist      -- dictionary mapping node label to length of minimum path from
                 s->node
    top_order -- topological ordering produced by subcall to topsort (can be
                 ignored if desired)

    """

    dist = {node: float('inf') for node in nodes}
    dist[start] = 0

    top_order = topsort(g)
    for u in top_order:
        for v in g[u]:
            dist[v] = min(dist[v], dist[u] + weights[u][v])

    return dist, top_order
