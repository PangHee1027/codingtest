import re

def solution(myStr):
    split_list = [x for x in re.split(r'(?:a|b|c)', myStr) if x]
    return ['EMPTY'] if not split_list else split_list