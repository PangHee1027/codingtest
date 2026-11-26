def colatz(n) :
    if n % 2 :
        return 3 * n + 1
    else :
        return n // 2

def solution(n) :
    answer = [n]
    while n > 1 :
        n = colatz(n)
        answer.append(n)
    return answer