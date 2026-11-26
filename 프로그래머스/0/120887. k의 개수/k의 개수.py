def solution(i, j, k):
    answer = 0
    l = ''
    for x in range(i, j + 1) :
        l += str(x)
    return l.count(str(k))