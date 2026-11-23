def solution(elements):
    s = set()
    n = len(elements)
    
    
    for i in range(n) :
        for j in range(n - i) :
            s.add(sum(elements[i : j + i]))
    return len(s)