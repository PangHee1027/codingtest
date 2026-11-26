def solution(arr):
    if 2 not in arr :
        return [-1]
    if arr[-1] == 2 :
        return arr[arr.index(2) :]
    return arr[arr.index(2) : -list(reversed(arr)).index(2)]