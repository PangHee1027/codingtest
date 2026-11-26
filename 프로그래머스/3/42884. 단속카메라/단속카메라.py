def solution(routes):
    routes.sort(key = lambda x : x[1])
    answer = 0
    last_end = -float("inf")

    for s, e in routes :
        if s > last_end:
            answer += 1
            last_end = e

    return answer