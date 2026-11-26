def solution(arr):
    stk = [arr[0]]
    i = 0
    n = len(arr)
    while i < n :
        if not stk :
            stk.append(arr[i])
            i += 1
        if stk[-1] < arr[i] :
            stk.append(arr[i])
            i += 1
        else :
            stk.pop()
    return stk