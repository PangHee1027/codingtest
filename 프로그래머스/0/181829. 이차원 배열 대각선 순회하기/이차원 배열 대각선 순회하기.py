def solution(board, k):
    answer = 0
    h, w = len(board), len(board[0])
    
    for i in range(h) :
        for j in range(w) :
            if i + j <= k :
                answer += board[i][j]
    return answer