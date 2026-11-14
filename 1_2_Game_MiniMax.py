
board = 7

def minimax(ismax, alpha, beta):
    global board

    if board <= 0 and not ismax:
        return 1, None

    if board <= 0 and ismax:
        return -1, None

    if ismax:
        best = float('-inf')
        bestmove = None

        for i in range(1, 3):
            board -= i

            if board < 0:
                board += i
                continue

            val, _ = minimax(False, alpha, beta)

            board += i

            if best < val:
                best = val
                bestmove = i

            alpha = max(alpha, best)

            if alpha >= beta:
                break

    else:
        best = float('inf')
        bestmove = None

        for i in range(1, 3):
            board -= i

            if board < 0:
                board += i
                continue

            val, _ = minimax(True, alpha, beta)

            board += i

            if best > val:
                best = val
                bestmove = i

            beta = min(beta, best)

            if alpha >= beta:
                break

    return best, bestmove


val, move = minimax(True, float('-inf'), float('inf'))
print("Computer:", move)
board -= move

# Human makes a move
move = 2
print("Human:", move)
board -= move

val, move = minimax(True, float('-inf'), float('inf'))
print("Computer:", move)
board -= move

print("Remaining stones:", board)
