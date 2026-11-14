
from collections import deque

# Accept number of cities
n = int(input("Enter number of cities: "))

# Accept city names
cities = input("Enter city names: ").split()

# Create adjacency list
graph = {city: [] for city in cities}

# Accept number of connections
e = int(input("Enter number of connections: "))

# Accept connections
for i in range(e):
    u, v = input(f"Enter connection {i+1}: ").split()

    graph[u].append(v)
    graph[v].append(u)  # Undirected graph

# Accept starting city
start = input("Enter starting city: ")

# BFS traversal
def BFS(start):

    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:

        node = queue.popleft()
        print(node, end=" ")

        for neighbour in graph[node]:

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


print("\nBFS Traversal:")
BFS(start)
