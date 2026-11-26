def solution(hp):
    answer = 0
    for n in (5, 3, 1) :
        answer += hp // n
        hp %= n
    return answer