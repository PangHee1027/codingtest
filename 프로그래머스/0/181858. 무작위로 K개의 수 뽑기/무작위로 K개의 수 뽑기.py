def solution(arr, k):
    stack = []
    for n in arr :
        if n in stack :
            continue
        stack.append(n)
        if len(stack) == k :
            return stack
    stack += [-1] * (k - len(stack))
    return stack