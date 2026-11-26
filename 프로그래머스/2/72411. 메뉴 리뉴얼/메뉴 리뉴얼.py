from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for c in course:
        counter = Counter()
        for order in orders:
            # 각 주문에서 c개짜리 조합을 모두 구함 (알파벳 정렬 필수)
            for comb in combinations(sorted(order), c):
                counter[comb] += 1
                
        if not counter:
            continue
            
        # 가장 많이 주문된 횟수 찾기 (단, 최소 2명 이상이어야 함)
        max_count = max(counter.values())
        if max_count >= 2:
            for comb, count in counter.items():
                if count == max_count:
                    answer.append("".join(comb))
                    
    # 최종 결과를 사전 순으로 정렬하여 리턴
    return sorted(answer)