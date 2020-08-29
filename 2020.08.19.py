# def solution(phone_number):
#     secret= len(phone_number)*"*"
#     num=len(secret)-4
#     result=num*"*"
#     answer=result+phone_number[-4:]
#     print(answer)
    
# solution("12345678")

def solution(phone_number):
    secret= len(phone_number)-4
    answer=secret*"*" + phone_number[-4:]
   
   
    print(answer)
    
solution("29880887")