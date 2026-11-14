board = [
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', ''],
    ['', '', '', '']
]

def check(r, c):
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                if r == i and c == j:
                    continue
                if c == j:
                    return False
                if (i - j) == (r - c):
                    return False
                if (i + j) == (r + c):
                    return False
    return True

def csp (row):
    for j in range(4):
        if check(row, j):
            board[row][j] = 'Q'
            if row<3:
                if csp(row+1):
                    return True
                else:
                    board[row][j] = ''
            else:
                return True
            
    return False

csp (0)

print(board)