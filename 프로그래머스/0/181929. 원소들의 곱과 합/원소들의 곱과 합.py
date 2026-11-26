def solution(숫자_리스트):
    곱 = 1
    for 숫자 in 숫자_리스트 :
        곱 *= 숫자
    return 1 if sum(숫자_리스트) ** 2 > 곱 else 0