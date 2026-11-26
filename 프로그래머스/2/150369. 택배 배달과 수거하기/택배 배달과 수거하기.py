import math

def solution(cap, n, deliveries, pickups):
    distance = 0
    delivery_remain = 0
    pickup_remain = 0
    
    for i in range(n - 1, -1, -1):
        delivery_remain += deliveries[i]
        pickup_remain += pickups[i]

        # 배달과 수거 중 더 많이 남은 양을 기준으로 필요한 왕복 횟수(cnt) 계산
        if delivery_remain > 0 or pickup_remain > 0:
            # 파이썬의 math.ceil을 사용하거나 정수 연산으로 올림 처리
            cnt = max(
                math.ceil(delivery_remain / cap),
                math.ceil(pickup_remain / cap)
            )
            
            distance += (i + 1) * 2 * cnt
            
            # 처리한 만큼 남은 물량 차감
            delivery_remain -= cap * cnt
            pickup_remain -= cap * cnt
            
    return distance