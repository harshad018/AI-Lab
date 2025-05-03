import sys

def tsp_nearest_neighbour(graph, start = 0):

    n = len(graph)
    visited = [False] * n
    path = [start]
    totalcost = 0

    visited[start] = True
    current = start

    for i in range (n-1):

        nearest = -1
        min_distance = sys.maxsize

        for i in range (n):

            if not visited[i] and 0 < graph[current][i] < min_distance:

                nearest = i
                min_distance = graph[current][i]



        visited[nearest] = True
        path.append(nearest)
        totalcost += min_distance
        current = nearest

    totalcost += graph[current][start]
    path.append(start)
    return path, totalcost



#input

graph = [

    [0,29,20,21],
    [29,0,15,17],
    [20,15,0,28],
    [21, 17, 28, 0]



]

path , cost = tsp_nearest_neighbour(graph)

print("Path: ", path)
print("Cost: ", cost)
