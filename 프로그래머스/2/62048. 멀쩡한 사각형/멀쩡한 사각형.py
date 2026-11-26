def get_gnb(a, b) :
    while b > 0 :
        a, b = b, a % b
    return a

def get_unusable(a, b) :
    if a == 1 or b == 1 :
        return max(a, b)

def solution(w,h):
    extent = w * h
    gnb = get_gnb(w, h)
    a, b = w // gnb, h // gnb
    answer = 1
    diagonal = a + b - 1
    return extent - (diagonal * gnb)