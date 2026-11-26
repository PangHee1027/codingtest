def solution(my_string, indices):
    my_string = list(my_string)
    indices.sort(reverse = True)
    
    for i in indices :
        my_string.pop(i)
        
    return "".join(my_string)