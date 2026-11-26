from collections import Counter

def solution(array):
    counter = dict(Counter(array))
    max_count = max(counter.values())
    
    max_item = 0
    
    for k, v in counter.items() :
        if v == max_count :
            if max_item :
                return -1
            max_item = k
    
    return max_item