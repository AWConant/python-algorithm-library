from ..array import sparsetable

class LCAStaticTree(object):
    """
    Reduces lowest common ancestor problem on an unchanging tree to the RMQ
    problem. Uses a Sparse Table to answer LCA queries efficiently.
    Time complexity:
      Construction: O(n*lg(n))
      Query: O(1)
    Space complexity: O(n*lg(n))

    tree -- a graph as an adjacency list. assumed to be an undirected tree
    root -- the label of the root node
    """
    def __init__(self, tree, root):
        self.tree = tree
        self.root = root

        self.first_idx = dict()
        self.euler_walk = []
        self.depth_array = []
        self._perform_euler_walk()
        self.rmq_handler = sparsetable.SparseTable(self.depth_array, sparsetable.rmq_idx, True)

    def query(self, node1, node2):
        """
        Return the lowest common ancestor of node1 and node2 efficiently.
        Time complexity: O(1)
        Space complexity: O(1)

        node1 -- a node present in the tree
        node2 -- another node present in the tree
        """
        if self.first_idx[node1] > self.first_idx[node2]:
            node1, node2 = node2, node1
        idx_of_min_depth = self.rmq_handler.query(self.first_idx[node1], self.first_idx[node2])
        return self.euler_walk[idx_of_min_depth]

    def _perform_euler_walk(self):
        stack = [(self.root, None, 0, False)]
        idx = 0

        while stack:
            node, prev, depth, backtracking = stack.pop()

            if node not in self.first_idx:
                self.first_idx[node] = idx

            self.depth_array.append(depth)
            self.euler_walk.append(node)

            idx += 1

            for neighbor in self.tree[node]:
                if neighbor != prev and not backtracking:
                    stack.append((node, prev, depth, True))
                    stack.append((neighbor, node, depth+1, False))
