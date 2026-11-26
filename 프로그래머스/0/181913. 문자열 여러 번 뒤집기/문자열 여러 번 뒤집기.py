def solution(my_string, queries):
    my_string = list(my_string)
    for s, e in queries :
        my_string = my_string[:s] + list(reversed(my_string[s:e + 1])) + my_string[e+1 :]
    return "".join(my_string)