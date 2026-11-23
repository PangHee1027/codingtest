def solution(arr):
    stack = []
    for n in arr :
        if not stack :
            stack.append(n)
            continue
        if n == stack[-1] :
            continue
        stack.append(n)
    return stack