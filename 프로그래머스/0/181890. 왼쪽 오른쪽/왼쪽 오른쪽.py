def solution(str_list):
    stack = []
    for i, s in enumerate(str_list) :
        if s == 'l' :
            return stack
        elif s == 'r' :
            return str_list[i + 1:]
        else :
            stack.append(s)
    return []