def solution(ineq, eq, n, m) :
    match (ineq, eq):
        case ('>', '=') :
            return int(n >= m)
        case ('<', '=') :
            return int(n <= m)
        case ('>', '!') :
            return int(n > m)
        case ('<', '!') :
            return int(n < m)