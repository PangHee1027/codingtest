def solution(a, b, c):
    s = {a, b, c}
    if len(s) == 1 :
        return 27 * (a ** 6)      
    if len(s) == 2 :
        return sum([a, b, c]) * sum([a ** 2, b ** 2, c ** 2])
    return a + b + c  