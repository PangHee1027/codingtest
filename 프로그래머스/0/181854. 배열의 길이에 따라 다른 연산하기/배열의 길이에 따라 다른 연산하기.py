def solution(arr, n):
    return [x + n if i % 2 else x for i, x in enumerate(arr)] if not len(arr) % 2 else [x + n if not i % 2 else x for i, x in enumerate(arr)]