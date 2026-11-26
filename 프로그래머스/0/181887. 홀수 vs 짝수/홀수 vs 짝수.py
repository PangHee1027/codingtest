def solution(num_list):
    return max(sum(x for i, x in enumerate(num_list) if i % 2), sum(x for i, x in enumerate(num_list) if not i % 2))