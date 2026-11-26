from collections import deque

def solution(rows, columns, queries):
    board = [[j + i * columns for j in range(1, columns + 1)] for i in range(0, rows)]
    answer = []

    for x1, y1, x2, y2 in queries :
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        dq = deque()
        l = []
        for i in range(y1, y2 + 1) :
            dq.append(board[x1][i])
            l.append(board[x1][i])
            if i == y1 :
                continue
            board[x1][i] = dq.popleft()
        for i in range(x1 + 1, x2 + 1) :
            dq.append(board[i][y2])
            l.append(board[i][y2])
            board[i][y2] = dq.popleft()
        for i in range(y2 - 1, y1 - 1, -1) :
            dq.append(board[x2][i])
            l.append(board[x2][i])
            board[x2][i] = dq.popleft()
        for i in range(x2 - 1, x1 - 1, -1) :
            dq.append(board[i][y1])
            l.append(board[i][y1])
            board[i][y1] = dq.popleft()
        answer.append(min(l))

    return answer