def solution(n):
    def convert(num):
        digits = "412"
        result = ""
            
        while num > 0:
            num, remainder = divmod(num, 3)
            if not remainder :
                num -= 1
            result = digits[remainder] + result
                
        return result
    
    return convert(n)