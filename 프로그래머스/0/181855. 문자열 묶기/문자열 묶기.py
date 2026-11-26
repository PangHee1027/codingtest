from collections import Counter

def solution(strArr):  
    return sorted(dict(Counter(len(x) for x in strArr)).items(), key = lambda x : x[1])[-1][1]