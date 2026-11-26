from math import isqrt

def is_prime(n) :
    qrt_n = isqrt(n)
    
    for i in range(2, qrt_n + 1) :
        if not n % i :
            return False
    
    return True

def solution(n):
    return sum(1 for x in range(4, n + 1) if not is_prime(x))