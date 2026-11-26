def solution(chicken):
    service = 0
    while chicken >= 10 :
        chicken, coupon = divmod(chicken, 10)
        service += chicken
        chicken += coupon
    return service