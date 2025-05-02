import sys

def tsp_nearest_neighbor(graph, start=0):
    n = len(graph)
    visited = [False] * n
    path = [start]
    total_cost = 0
    visited[start] = True
    current = start

    for _ in range(n - 1):
        nearest = -1
        min_dist = sys.maxsize
        for i in range(n):
            if not visited[i] and 0 < graph[current][i] < min_dist:
                nearest = i
                min_dist = graph[current][i]
        path.append(nearest)
        visited[nearest] = True
        total_cost += min_dist
        current = nearest

    # Return to start
    total_cost += graph[current][start]
    path.append(start)
    return path, total_cost

# Default distance matrix (can be changed)
graph = [
    [0, 29, 20, 21],
    [29, 0, 15, 17],
    [20, 15, 0, 28],
    [21, 17, 28, 0]
]

path, cost = tsp_nearest_neighbor(graph)
print("Tour path:", path)
print("Total cost:", cost)
