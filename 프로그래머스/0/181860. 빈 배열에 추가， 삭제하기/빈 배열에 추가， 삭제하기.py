def solution(arr, flag):
    n = len(arr)
    X = []
    for i in range(n) :
        if flag[i] :
            X += [arr[i]] * arr[i] * 2
        else :
            for _ in range(arr[i]) :
                X.pop()
    return X