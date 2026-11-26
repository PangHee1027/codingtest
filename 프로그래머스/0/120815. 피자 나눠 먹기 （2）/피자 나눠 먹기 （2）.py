def get_lcm(a, b) :
    multi = a * b
    while b > 0 :
        a, b = b, a % b
    return multi // a

def solution(n):
    return get_lcm(6, n) // 6