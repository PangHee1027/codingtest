def solution(arr, idx):
    string = "".join(map(str, arr))
    return string.find("1", idx)