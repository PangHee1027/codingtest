def solution(slice, n):
    pizza = slice
    count = 1
    while pizza < n :
        pizza += slice
        count += 1
    return count