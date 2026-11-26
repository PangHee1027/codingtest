import math

def solution(n):
    answer = []
    qrt_n = math.isqrt(n)
    for i in range(1, qrt_n + 1) :
        if not n % i :
            answer.append(i)
            if n // i > i :
                answer.append(n // i)
    answer.sort()
    
    return answer