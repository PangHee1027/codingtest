def solution(polynomial):
    x, b = 0, 0
    answer = ''
    polynomial = polynomial.replace("+", "").split()
    
    for p in polynomial :
        if 'x' in p :
            x += int(p[:-1]) if p[:-1] else 1
        else :
            b += int(p)

    if x :
        answer += (str(x) + 'x') if x != 1 else 'x'
    if b :
        answer += (' + ' + str(b)) if answer else str(b)
        
    return answer