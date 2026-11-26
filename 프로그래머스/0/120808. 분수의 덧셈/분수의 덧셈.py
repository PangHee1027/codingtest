# 유클리드 호제법
def get_gcd (a, b) :
    while b != 0 :
        a, b = b, a % b
    return a

# 추가 팁
# 최소 공배수 = a * b // gcd
def solution(numer1, denom1, numer2, denom2):
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd = get_gcd(numer, denom)
    
    return [numer // gcd, denom // gcd]