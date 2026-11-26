from collections import deque

def solution(players, m, k):
    answer = 0
    server = deque([0 for _ in range(k)], maxlen=k)

    for i, player in enumerate(players) :
        server.popleft()
        require = 0
        while player >= m * (sum(server) + require) + m :
            require +=1
        answer += require
        server.append(require)
    return answer