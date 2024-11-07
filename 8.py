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

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()  # Set to keep track of visited nodes

        visited.add(start)  # Mark the current node as visited
        print(start, end=' ')  # Process the node

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)

    print("DFS starting from node 0:")
    g.dfs(0)
