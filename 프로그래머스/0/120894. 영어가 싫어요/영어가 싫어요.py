import re

def solution(numbers):
    # 영단어와 대응하는 숫자를 담은 딕셔너리
    digit = {
        'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    
    # 1. 딕셔너리의 키들을 '|'(OR) 기호로 묶어서 하나의 패턴으로 만듦
    # 결과 패턴: 'zero|one|two|three|four|five|six|seven|eight|nine'
    pattern = '|'.join(digit.keys())
    
    # 2. re.sub를 이용해 패턴과 일치하는 부분을 찾아 딕셔너리의 값으로 치환
    result = re.sub(pattern, lambda m: digit[m.group(0)], numbers)
    
    return int(result)