def solution(age):
    digits = 'abcdefghij'
    return "".join(digits[int(x)] for x in str(age))