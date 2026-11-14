
import heapq

graph = {
    'S': [('A', 2), ('B', 5)],
    'A': [('C', 4), ('D', 7)],
    'B': [('C', 2), ('E', 3)],
    'C': [('G', 5)],
    'D': [('G', 4)],
    'E': [('G', 6)],
    'G': []
}

heuristic = {
    'S': 8, 'A': 6, 'B': 5,
    'C': 3, 'D': 2, 'E': 4, 'G': 0
}

def astar(graph, heuristic, start, goal):

    pq = []
    heapq.heappush(pq, (heuristic[start], 0, start, [start]))

    visited = set()
    best_g = {start: 0}

    step = 1

    while pq:

        f, g, node, path = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)

        h = heuristic[node]

        print(f"Step {step}: {node}")
        print(f"Path: {path}")
        print(f"g(n) = {g}, h(n) = {h}, f(n) = {f}")
        print()

        step += 1

        if node == goal:
            print("Optimal Path:", path)
            print("Total Path Cost:", g)
            return path, g

        for neighbour, cost in graph[node]:

            new_g = g + cost

            if neighbour not in visited and new_g < best_g.get(neighbour, float('inf')):

                best_g[neighbour] = new_g
                new_f = new_g + heuristic[neighbour]

                heapq.heappush(
                    pq,
                    (new_f, new_g, neighbour, path + [neighbour])
                )

    return None, float('inf')


astar(graph, heuristic, 'S', 'G')
