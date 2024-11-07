from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def bfs(self, start):
        visited = set()  # Set to keep track of visited nodes
        queue = deque([start])  # Initialize the queue with the start node
        visited.add(start)

        while queue:
            node = queue.popleft()  # Dequeue a vertex from the queue
            print(node, end=' ')  # Process the node

            # Get all adjacent vertices of the dequeued node
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark as visited
                    queue.append(neighbor)  # Enqueue the neighbor

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    print("BFS starting from node 0:")
    g.bfs(0)
