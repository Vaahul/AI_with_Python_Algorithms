board = [
    ['X', '', ''],
    ['', '', ''],
    ['', '', '']
]


def check():
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            return board[0][i]

        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            return board[i][0]

    if board[0][0] == board[1][1] == board[2][2] and board[1][1]:
        return board[1][1]

    if board[0][2] == board[1][1] == board[2][0] and board[1][1]:
        return board[1][1]

    return False


def full():
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                return False
    return True


def minimax(ismax, alpha, beta):

    if check() == 'X':
        return 1, None

    elif check() == 'O':
        return -1, None

    if full():
        return 0, None

    if ismax:
        best = float('-inf')
        bestnode = None

        for i in range(3):
            for j in range(3):

                if not board[i][j]:
                    board[i][j] = 'X'

                    val, _ = minimax(False, alpha, beta)

                    board[i][j] = ''

                    if val > best:
                        best = val
                        bestnode = [i, j]

                    alpha = max(alpha, best)

                    if alpha >= beta:
                        break

            if alpha >= beta:
                break

    else:
        best = float('inf')
        bestnode = None

        for i in range(3):
            for j in range(3):

                if not board[i][j]:
                    board[i][j] = 'O'

                    val, _ = minimax(True, alpha, beta)

                    board[i][j] = ''

                    if val < best:
                        best = val
                        bestnode = [i, j]

                    beta = min(beta, best)

                    if alpha >= beta:
                        break

            if alpha >= beta:
                break

    return best, bestnode

best, bestnode = minimax(0, float('-inf'), float('inf'))

board[bestnode[0]][bestnode[1]] = 'O'

print(board)