def solution(arr):
    stk = []
    i =  0
    n = len(arr)
    while i < n :
        if not stk :
            stk.append(arr[i])
        elif stk[-1] == arr[i] :
            stk.pop()
        elif stk[-1] != arr[i] :
            stk.append(arr[i])
        i += 1
            
    return stk if stk else [-1]