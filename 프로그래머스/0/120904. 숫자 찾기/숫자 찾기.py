def solution(num, k):
    num = str(num)
    if str(k) not in num :
        return -1
    return num.index(str(k)) + 1