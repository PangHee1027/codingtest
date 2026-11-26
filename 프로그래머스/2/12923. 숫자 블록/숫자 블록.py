def solution(begin, end):
    length = end - begin + 1
    
    # 1인 경우는 0, 그 외에는 기본적으로 1로 초기화 (1은 모든 수의 약수이므로)
    answer = [0 if (begin + i) == 1 else 1 for i in range(length)]
    
    # 탐색할 수 있는 최대 블록 번호는 10,000,000 이며, 어떤 수의 약수는 그 수의 절반을 넘을 수 없음
    limit = min(10_000_000, end // 2)
    
    # 2부터 limit까지의 숫자를 '블록 번호(약수)'로 가정하고 배수들을 순회
    for i in range(2, limit + 1):
        # i의 배수 중 [begin, end] 범위에 속하는 가장 작은 k와 가장 큰 k 계산
        start_k = max(2, (begin + i - 1) // i)
        end_k = end // i
        
        for k in range(start_k, end_k + 1):
            pos = i * k
            idx = pos - begin
            
            # i와 k는 모두 pos의 약수이므로, 10,000,000 이하인 경우 최댓값 갱신
            if i <= 10_000_000 and i > answer[idx]:
                answer[idx] = i
            if k <= 10_000_000 and k > answer[idx]:
                answer[idx] = k
                
    return answer