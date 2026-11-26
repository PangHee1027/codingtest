def solution(my_strings, parts):
    return "".join(str[parts[i][0] : parts[i][1] + 1] for i, str in enumerate(my_strings))