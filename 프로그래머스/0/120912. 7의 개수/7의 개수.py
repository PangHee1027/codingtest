def solution(array):
    result = ''
    for n in array :
        result += str(n)
    return result.count('7')