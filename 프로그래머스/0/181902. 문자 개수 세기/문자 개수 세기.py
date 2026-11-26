import string

def solution(my_string):
    strings = string.ascii_uppercase + string.ascii_lowercase
    return [my_string.count(x) for x in strings]