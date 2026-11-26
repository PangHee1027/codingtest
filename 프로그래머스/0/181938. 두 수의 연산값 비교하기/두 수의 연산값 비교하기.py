def solution(a, b):
    return max(a * (10 ** len(str(b))) + b , 2 * a * b)