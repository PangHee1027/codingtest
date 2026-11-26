def solution(names):
    return [x for i, x in enumerate(names) if not i % 5]