def solution(numbers, direction):
    return ([numbers[-1]] + numbers[:-1]) if direction.startswith('r') else (numbers[1:] + [numbers[0]]) 