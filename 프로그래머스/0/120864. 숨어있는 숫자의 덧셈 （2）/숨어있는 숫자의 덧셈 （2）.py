def solution(my_string):
    answer = 0
    stack = []
    for s in my_string :
        if stack and not s.isdigit() :
            answer += int("".join(stack))
            stack = []
        if s.isdigit() :
            stack.append(s)
    if stack :
        answer += int("".join(stack))
    return answer