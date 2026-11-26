def facto(i) :
    if i == 1 :
        return 1
    return facto(i - 1) * i

def solution(n):
    for i in range(1, 12) :
        if facto(i) > n :
            return i - 1