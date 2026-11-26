def solution(strArr) :
    answer = []
    for i, str in enumerate(strArr) :
        answer.append(str.upper() if i % 2 else str.lower())
            
    return answer