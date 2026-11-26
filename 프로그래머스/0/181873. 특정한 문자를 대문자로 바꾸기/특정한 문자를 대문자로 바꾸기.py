def solution(my_string, alp):
    my_string = list(my_string)
    for i, s in enumerate(my_string) :
        if s == alp :
            my_string[i] = chr(ord(s) - 32)
    return "".join(my_string)