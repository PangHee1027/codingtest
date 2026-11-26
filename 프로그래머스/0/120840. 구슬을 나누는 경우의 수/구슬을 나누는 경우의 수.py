def solution(balls, share):
    facto = [0] * (balls + 1)
    facto[0], facto[1] = 1, 1
    for i in range(2, balls + 1) :
        facto[i] = facto[i - 1] * i
    return facto[balls] // (facto[balls - share] * facto[share])