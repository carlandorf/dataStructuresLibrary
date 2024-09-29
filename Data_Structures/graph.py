# data_structures/graph.py

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        """Add a new vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices."""
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        """Remove a vertex and all connected edges."""
        if vertex in self.graph:
            # Remove all edges connected to this vertex
            for adjacent in self.graph[vertex]:
                self.graph[adjacent].remove(vertex)
            # Remove the vertex itself
            del self.graph[vertex]

    def remove_edge(self, vertex1, vertex2):
        """Remove the edge between two vertices."""
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def bfs(self, start_vertex):
        """Perform BFS traversal starting from start_vertex."""
        visited = set()
        queue = [start_vertex]
        result = []

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                # Enqueue all unvisited neighbors
                queue.extend([v for v in self.graph[vertex] if v not in visited])

        return result

    def dfs(self, start_vertex):
        """Perform DFS traversal starting from start_vertex."""
        visited = set()
        stack = [start_vertex]
        result = []

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                # Push all unvisited neighbors onto the stack
                stack.extend([v for v in self.graph[vertex] if v not in visited])

        return result

    def __str__(self):
        """String representation of the graph."""
        return str(self.graph)