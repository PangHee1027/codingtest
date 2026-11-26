def solution(문자열, 찾는거):
    딕셔너리 = {"A" : "B", "B" : "A"}
    
    바꾼_문자열 = ""
    for 문자 in 문자열 :
        바꾼_문자열 += 딕셔너리[문자]
        
    return 1 if 찾는거 in 바꾼_문자열 else 0