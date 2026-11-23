# 아 뭔가 집중하기 싫어졌으, 집중하면 풀겠는데 머리 쓰기가 싫다
def solution(s):
    answer = 0
    target = ''
    count = 0
    for c in s :
        if not target :
            target = c
            count = 1
            continue
        if c == target :
            count += 1
        else :
            count -= 1
        if not count :
            target = ''
            count = 1
            answer += 1
    if target :
        answer += 1
    return answer