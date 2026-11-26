import math

def is_prime(n) :
    qrt_n = math.isqrt(n)
    
    for i in range(2, qrt_n + 1) :
        if not n % i :
            return False
    return True

def solution(n) :
    division = []
    qrt_n = math.isqrt(n)
    for i in range(1, qrt_n + 1) :
        if not n % i :
            division.append(i)
            if n // i > i :
                division.append(n // i)
    answer = [x for x in division if is_prime(x)]
    return sorted(answer)[1:]