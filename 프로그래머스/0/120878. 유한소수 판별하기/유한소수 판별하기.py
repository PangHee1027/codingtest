import math

def get_gcd(a, b) :
    while b :
        a, b = b, a % b
    return a

def get_divisor(n) :
    qrt_n = math.isqrt(n)
    result = []
    for i in range(1, qrt_n + 1) :
        if not n % i :
            result.append(i)
            if n // i > i :
                result.append(n // i)
                
    return result

def is_prime(n) :
    qrt_n = math.isqrt(n)
    for i in range(2, qrt_n + 1) :
        if not n % i :
            return False
    return True

def solution(a, b):
    gcd = get_gcd(a, b)
    denom = b // gcd
    
    if denom == 1 :
        return 1
    
    divisor = [x for x in get_divisor(denom) if is_prime(x) and not (x == 2 or x == 5 or x == 1)]
    print(divisor)
    if divisor :
        return 2
    
    return 1
