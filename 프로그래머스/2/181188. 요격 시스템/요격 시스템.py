def solution(targets):
    # 1. 미사일을 끝점(e) 기준으로 오름차순 정렬
    targets.sort(key=lambda x: x[1])
    
    answer = 0
    last_end = -1  # 마지막으로 요격 미사일을 쏜 위치
    
    for s, e in targets:
        # 현재 미사일의 시작점이 직전 요격 위치보다 크거나 같으면 새로운 미사일 필요
        if s >= last_end:
            answer += 1
            last_end = e  # 새로운 요격 미사일을 현재 미사일의 끝점에 설치
            
    return answer