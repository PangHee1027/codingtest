def solution(M, N):
    return min((M-1) + M * (N - 1), (N-1) + N * (M - 1))