def solution(dot):
    answer = 0
    dot = (dot[0] // abs(dot[0]), dot[1] // abs(dot[1]))
    match dot :
        case (1, 1) :
            answer = 1
        case (-1, 1) :
            answer = 2
        case (-1, -1) :
            answer = 3
        case (1, -1) :
            answer = 4
    return answer