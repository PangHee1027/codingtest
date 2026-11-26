def solution(s):
    stack = []
    s = s.split()
    
    for c in s :
        if c == "Z" :
            stack.pop()
        else :
            stack.append(c)
    return sum(map(int, stack))