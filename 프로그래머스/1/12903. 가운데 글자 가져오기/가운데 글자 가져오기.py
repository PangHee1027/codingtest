def solution(s):
    n = len(s)
    i = n // 2
    if n % 2 :
        return (s[i])
    return s[i - 1 : i + 1]