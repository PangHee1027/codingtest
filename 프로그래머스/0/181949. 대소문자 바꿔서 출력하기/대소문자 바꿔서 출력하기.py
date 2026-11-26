str = input()
answer = ''

for s in str :
    if ord('a') <= ord(s) <= ord('z') :
        answer += s.upper()
    else :
        answer += s.lower()
        
print(answer)