def solution(numbers):
    if not max(numbers) :
        return "0"
    numbers_str = list(map(str, numbers))
    numbers_str.sort(reverse = True, key = lambda x : x * 3)
    
    return "".join(numbers_str)