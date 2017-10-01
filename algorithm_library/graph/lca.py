from ..array import rmq

class LCAStaticTree(object):
    def __init__(self, graph, node_count, root):
        self.graph = graph
        self.node_count = node_count
        self.root = root

        self.first_idx = dict()
        self.euler_walk = []
        self.depth_array = []
        self._perform_euler_walk()
        self.rmq_handler = rmq.RMQStaticArray(self.depth_array)

    def query(self, node1, node2):
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

            for neighbor in self.graph[node]:
                if neighbor != prev and not backtracking:
                    stack.append((node, prev, depth, True))
                    stack.append((neighbor, node, depth+1, False))
