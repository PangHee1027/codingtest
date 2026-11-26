import math

def solution(n):
    qrt_n = math.isqrt(n)
    answer = 0
    
    for i in range(1, qrt_n + 1) :
        if not n % i :
            answer += 1
            if n // i > i :
                answer += 1
    return answer