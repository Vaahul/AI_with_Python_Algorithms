
import random

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['H'],
    'F': None,
    'G': ['H'],
    'H': ['I'],
    'I': ['J'],
    'J': None
}

heuristic = {
    'A': 9,
    'B': 7,
    'C': 8,
    'D': 5,
    'E': 6,
    'F': 4,
    'G': 4,
    'H': 4,
    'I': 2,
    'J': 0
}

visited = []


def HillClimbing(node, restarts):

    visited.append(node)

    if node == 'J':
        return True

    if graph[node]:
        for i in graph[node]:

            if heuristic[i] < heuristic[node]:
                if HillClimbing(i, restarts):
                    return True

    # No better neighbour: restart
    if restarts > 0:

        print(f"Stuck at {node}. Restarting...")

        visited.clear()

        new_node = random.choice(list(graph.keys()))

        return HillClimbing(new_node, restarts - 1)

    return False


if HillClimbing('A', 5):
    print("Goal reached!")
else:
    print("Maximum restarts reached.")

print("Path:", visited)
