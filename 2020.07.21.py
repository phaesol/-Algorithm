#중복 알고리즘 풀기-실패..

# answer = []
# def solution(a):
#    for i in range(len(a)):
#     if i ==0 :
#        answer.append(i)
#        else i != i-1:
#        answer.append(i)
#         return answer

# print(solution("13333"))

#글자 수가 같으면 true, 아니면 false 리턴

# def solution(s):
#     # a=''
#     # s= a.upper()
#     if s.count('p')==s.count('y'):
#         return True
#     elif s.count('P') !=s.count('Y'):
#         return False
#     else:
#          True

# 문제 : p와 y를 대 소문자 구분없이 갯수를 세어 p와 y의 갯수가 같거나, 두 문자 모두 존재하지 않는 경우는 True를 ,
 #       p와 y의 갯수가 다르다면 False를 반환하여라. 
def solution(s):
      
    a=s.lower()   # a는 s변수의 소문자의 모음으로 정의해준다. 
   
    if a.count('p')==a.count('y'): #정의된 a의 특정 문자의 갯수를 세는 함수 count를 넣어 같으면 True를 반환한다. 0 도 0==0이므로 이에 해당.
        return True
    else:
        return False #나머지 경우인 갯수가 같지 않을 경우 False를 반환

print(solution("ppYyy")) #함수가 제대로 돌아가는지 보기 위해 s에 임의의 글자를 넣어주었다.







 

   


