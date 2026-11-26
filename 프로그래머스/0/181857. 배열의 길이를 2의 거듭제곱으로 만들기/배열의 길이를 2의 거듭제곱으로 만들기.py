def solution(arr):
    two_square = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
    min_two_square = list(x for x in two_square if x >= len(arr))[0]
    arr += [0] * (min_two_square - len(arr))
    return arr