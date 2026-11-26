def solution(lines):
    scale = -min(x[0] for x in lines)
    n = max(x[1] for x in lines)
    dp = [0] * (n + scale + 1)
    for s, e in lines :
        dp[s + scale] += 1
        dp[e + scale] -= 1
    for i in range(n + scale) :
        dp[i + 1] += dp[i]
        
    return sum(1 for x in dp if x >= 2)