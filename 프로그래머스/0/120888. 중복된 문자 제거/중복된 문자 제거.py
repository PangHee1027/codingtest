def solution(my_string):
    answer = ''
    already = set()
    
    for s in my_string :
        if s not in already :
            already.add(s)
            answer += s
    return answer