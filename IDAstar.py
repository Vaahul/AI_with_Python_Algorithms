
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


def ida_star(graph, heuristic, start, goal):

    threshold = heuristic[start]
    iteration = 1

    def dfs(node, g, path, threshold, explored):

        h = heuristic[node]
        f = g + h

        explored.append((node, g, h, f))

        # Check threshold
        if f > threshold:
            return f

        # Check goal
        if node == goal:
            return (path, g)

        min_exceeded = float('inf')

        for neighbour, cost in graph[node]:

            # Avoid cycles in the current path
            if neighbour not in path:

                result = dfs(
                    neighbour,
                    g + cost,
                    path + [neighbour],
                    threshold,
                    explored
                )

                # Goal found
                if isinstance(result, tuple):
                    return result

                # Find minimum exceeded f-value
                min_exceeded = min(min_exceeded, result)

        return min_exceeded

    while True:

        print(f"\nIteration {iteration}")
        print("Threshold:", threshold)

        explored = []

        result = dfs(start, 0, [start], threshold, explored)

        print("Nodes explored:")

        for node, g, h, f in explored:
            status = "CUTOFF" if f > threshold else "EXPANDED"
            print(f"{node}: g={g}, h={h}, f={f} ({status})")

        # Goal found
        if isinstance(result, tuple):
            path, cost = result
            print("\nFinal Path:", path)
            print("Total Path Cost:", cost)
            return path, cost

        # No solution possible
        if result == float('inf'):
            print("No solution found!")
            return None, float('inf')

        # Increase threshold
        threshold = result
        iteration += 1


ida_star(graph, heuristic, 'S', 'G')
