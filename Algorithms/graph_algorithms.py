# data_structures/graph_algorithms.py

def dfs(graph, start, visited=None):
    """Perform depth-first search on the graph starting from start vertex."""
    if visited is None:
        visited = set()
    visited.add(start)
    result = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    return result

def bfs(graph, start):
    """Perform breadth-first search on the graph starting from start vertex."""
    visited = set()
    queue = [start]
    result = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend([v for v in graph[vertex] if v not in visited])
    return result

def dijkstra(graph, start):
    """Compute the shortest path from start to all vertices in a weighted graph."""
    import heapq
    priority_queue = [(0, start)]
    distances = {start: 0}
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue
        visited.add(current_vertex)

        for neighbor, weight in graph.get(current_vertex, {}).items():
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances