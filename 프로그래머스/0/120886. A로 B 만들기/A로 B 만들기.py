from collections import Counter

def solution(before, after):
    before_counter = set(dict(Counter(before)).items())
    after_counter = set(dict(Counter(after)).items())
    return 1 if before_counter == after_counter else 0