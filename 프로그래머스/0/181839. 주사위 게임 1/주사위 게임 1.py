def solution(a, b):
    dict = {(1, 1) : a ** 2 + b ** 2, (1, 0) : 2 * (a + b), (0, 1) : 2 * (a + b), (0, 0) : abs(a - b)}
    return dict[(a % 2, b % 2)]