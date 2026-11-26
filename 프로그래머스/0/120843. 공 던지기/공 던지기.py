def solution(numbers, k):
    n = len(numbers)
    return 2 * (k - 1) % n + 1