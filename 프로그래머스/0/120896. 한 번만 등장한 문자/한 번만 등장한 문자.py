from collections import Counter

def solution(s) :
    return "".join(sorted([key for key, count in dict(Counter(s)).items() if count == 1]))