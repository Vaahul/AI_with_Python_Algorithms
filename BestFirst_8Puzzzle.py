
import heapq

start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]


# Calculate Manhattan Distance
def heuristic(board):
    distance = 0

    for i in range(3):
        for j in range(3):

            tile = board[i][j]

            if tile != 0:
                goal_row = (tile - 1) // 3
                goal_col = (tile - 1) % 3

                distance += abs(i - goal_row)
                distance += abs(j - goal_col)

    return distance


# Convert 2D list into tuple for visited set
def get_state(board):
    return tuple(tuple(row) for row in board)


def greedy_best_first(start, goal):

    # Priority queue: (heuristic, board, path)
    pq = []
    heapq.heappush(pq, (heuristic(start), 0, start, [start]))

    visited = set()

    # Possible movements of blank tile
    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    while pq:

        h, _, board, path = heapq.heappop(pq)

        state = get_state(board)

        if state in visited:
            continue

        visited.add(state)

        # Check goal
        if board == goal:
            print("Solution found!\n")

            for step, current in enumerate(path):
                print("Step", step)

                for row in current:
                    print(row)

                print()

            print("Total moves:", len(path) - 1)
            return

        # Find blank position
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    x, y = i, j

        # Generate neighboring states
        for dx, dy in moves:

            nx = x + dx
            ny = y + dy

            if 0 <= nx < 3 and 0 <= ny < 3:

                new_board = [row[:] for row in board]

                # Swap blank with adjacent tile
                new_board[x][y], new_board[nx][ny] = (
                    new_board[nx][ny],
                    new_board[x][y]
                )

                new_state = get_state(new_board)

                if new_state not in visited:

   
                    new_h = heuristic(new_board)

                    heapq.heappush(
                        pq,
                        (new_h, len(visited), new_board,
                            path + [new_board])
                    )

    print("No solution found!")


greedy_best_first(start, goal)
