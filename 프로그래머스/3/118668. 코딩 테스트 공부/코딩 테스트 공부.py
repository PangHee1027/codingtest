def solution(alp, cop, problems):
    target_alp = max(max(x[0] for x in problems), alp)
    target_cop = max(max(x[1] for x in problems), cop)
    
    dp = [[float('inf')] * (target_cop + 1) for _ in range(target_alp + 1)]
    
    start_alp = min(alp, target_alp)
    start_cop = min(cop, target_cop)
    dp[start_alp][start_cop] = 0

    for i in range(start_alp, target_alp + 1):
        for j in range(start_cop, target_cop + 1):
            if i < target_alp :
                dp[i + 1][j] = min(dp[i][j] + 1, dp[i + 1][j])
            if j < target_cop :
                dp[i][j + 1] = min(dp[i][j] + 1, dp[i][j + 1])
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems :
                if alp_req <= i and cop_req <= j :
                    clear_alp = min(i + alp_rwd, target_alp)
                    clear_cop = min(j + cop_rwd, target_cop)
                    dp[clear_alp][clear_cop] = min(dp[clear_alp][clear_cop], dp[i][j] + cost)

    return dp[target_alp][target_cop]