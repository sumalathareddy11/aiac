class Graph:
    """
    Graph implementation using an adjacency list.
    Supports BFS and both recursive and iterative DFS traversals.
    """
    def __init__(self):
        # The adjacency list is a dictionary mapping each node to a list of neighbors
        self.adj_list = {}

    def add_edge(self, u, v):
        """
        Add an edge from node u to node v (undirected by default).
        """
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)  # Comment this line for directed graph

    def bfs(self, start):
        """
        Breadth-First Search traversal from the start node.
        Returns a list of nodes in BFS order.
        """
        from collections import deque
        visited = set()
        queue = deque()
        order = []

        queue.append(start)
        visited.add(start)

        while queue:
            node = queue.popleft()  # FIFO: pop from left
            order.append(node)
            # Visit all unvisited neighbors
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs_recursive(self, start):
        """
        Depth-First Search (recursive) traversal from the start node.
        Returns a list of nodes in DFS order.
        """
        visited = set()
        order = []

        def dfs(node):
            visited.add(node)
            order.append(node)
            for neighbor in self.adj_list.get(node, []):
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start)
        return order

    def dfs_iterative(self, start):
        """
        Depth-First Search (iterative) traversal from the start node.
        Returns a list of nodes in DFS order.
        """
        visited = set()
        stack = []
        order = []

        stack.append(start)

        while stack:
            node = stack.pop()  # LIFO: pop from right
            if node not in visited:
                visited.add(node)
                order.append(node)
                # Add neighbors to stack (reverse for consistent order with recursion)
                for neighbor in reversed(self.adj_list.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return order

    def print_adjacency_list(self):
        """
        Print the adjacency list for debugging.
        """
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")

# Example usage and comparison
if __name__ == "__main__":
    g = Graph()
    # Create a sample undirected graph
    edges = [
        (0, 1), (0, 2), (1, 3), (1, 4),
        (2, 5), (2, 6)
    ]
    for u, v in edges:
        g.add_edge(u, v)

    print("Adjacency List:")
    g.print_adjacency_list()

    print("\nBFS traversal from node 0:", g.bfs(0))
    print("DFS Recursive traversal from node 0:", g.dfs_recursive(0))
    print("DFS Iterative traversal from node 0:", g.dfs_iterative(0))

    print("\nComparison of DFS Recursive vs Iterative:")
    print("  - Recursive DFS uses the call stack, is elegant and concise, but may hit recursion limits for large/deep graphs.")
    print("  - Iterative DFS uses an explicit stack, avoids recursion depth issues, and can be more flexible for custom traversal orders.")
