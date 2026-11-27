from collections import deque

def solution(players, m, k):
    dq = deque()
    n = len(dq)
    answer = 0
    server = m
    for player in players :
        if n >= k :
            minus = dq.popleft()
            server -= minus * m
            n -= 1
        if player >= server :
            necessary = player - server
            plus = (necessary + m) // m
            server += plus * m
            dq.append(plus)
            n += 1
            answer += plus
        else :
            dq.append(0)
            n += 1
        print(dq, server, player, answer)
    
    return answer