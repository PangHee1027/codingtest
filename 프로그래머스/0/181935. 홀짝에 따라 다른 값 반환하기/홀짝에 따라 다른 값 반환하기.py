def solution(n):
    if n % 2 :
        return sum(x for x in range(1, n + 1, 2))
    return sum(x ** 2 for x in range(0, n + 1, 2))