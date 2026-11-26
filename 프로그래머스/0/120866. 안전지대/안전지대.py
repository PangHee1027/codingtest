from itertools import product

def solution(board):
    n = len(board)
    danger = set()
    for i, row in enumerate(board):
        for j, x in enumerate(row):
            if not x:
                continue
            danger.update((i+di, j+dj) for di, dj in product([-1,0,1], repeat=2))
    return n*n - sum(0 <= i < n and 0 <= j < n for i, j in danger)