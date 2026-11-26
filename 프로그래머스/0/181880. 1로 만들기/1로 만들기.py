def solution(num_list):
    def devide_to_one(num) :
        count = 0
        while num > 1 :
            if num % 2 :
                num = (num - 1) // 2
            else :
                num //= 2
            count += 1
        return count
    return sum(devide_to_one(x) for x in num_list)