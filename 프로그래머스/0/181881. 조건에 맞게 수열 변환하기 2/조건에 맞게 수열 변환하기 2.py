def solution(arr):
    i = 0
    n = len(arr)
    while True :
        pre_arr = list(arr)
        for j in range(n) :
            num = arr[j]
            if num >= 50 and not num % 2 :
                arr[j] = num // 2
            elif num < 50 and num % 2 :
                arr[j] = num * 2 + 1
                
        if pre_arr == arr :
            return i
        i += 1
            
        