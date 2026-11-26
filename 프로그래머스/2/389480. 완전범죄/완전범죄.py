def solution(info, n, m):
    # dp[b] = B의 흔적이 b일 때, A가 얻을 수 있는 최소 흔적
    # B의 흔적은 m 미만이어야 하므로 크기는 m으로 설정하고 무한대로 초기화
    dp = [float('inf')] * m
    dp[0] = 0  # 초기 상태: A도 0, B도 0 흔적일 때 A의 흔적은 0
    
    for da, db in info:
        next_dp = [float('inf')] * m
        
        for b in range(m):
            if dp[b] == float('inf'):
                continue
            
            # 1. A도둑이 물건을 훔치는 경우
            next_a = dp[b] + da
            if next_a < n:  # A가 경찰에 붙잡히지 않는 경우(n 미만)만 허용
                next_dp[b] = min(next_dp[b], next_a)
            
            # 2. B도둑이 물건을 훔치는 경우
            next_b = b + db
            if next_b < m:  # B가 경찰에 붙잡히는 경우(m 미만)만 허용
                next_dp[next_b] = min(next_dp[next_b], dp[b])
                
        dp = next_dp
        
    # 모든 물건을 다 훔쳤을 때, 가능한 A의 최소 흔적 찾기
    min_a = min(dp)
    
    return min_a if min_a != float('inf') else -1