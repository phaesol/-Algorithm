# def solution(s, n):
#     s= 

#     answer = ''
#     return answer


# string.ascii_lowercase #모든 소문자 가져오기
# string.ascii_uppercase #모든 대문자 가져오기
# import string 

# result_list = []

# def solution(s,n):
   
#    # n = # 정의 어떻게 - result 자체가 우리가 위치의 숫자로 받아왔기 때문에 정의해줄 필요 X
#     s1 = list(string.ascii_letters)
#     # s2 = list(string.ascii_uppercase)
#     # # s = #어떻게 정의해야하지.. 어떻게 s1,s2 합치지 젠장
    
#     for i in s1:
#         result1 = s1.index(i) # 이렇게 되면 맨마지막값만 return하는 것
#         result_list.append(result1)
#         return chr(result1 +n) 
#     # for r in s2:
#     #     result2 = s2.index(r)
#     #     return chr(result2 +n)
        
# print(solution('AB',3))

# #for문으로 돌려주고 공백 split로 나누고 z는 기준 나눠준다.





# import string

# def solution(s,n):
    
#     s_list= s.split() 
    
#     for i in s_list:
    
#         if i in list(map(chr, range(97, 122))) :
        
#             return chr(ord(i)+n)
#         # b_list.append(s)  
          
    
#         elif i in list(map(chr, range(65, 90))) :
        
#             return chr(ord(i)+n)
#         # b_list.append(s)
       
#         else :
         
   
# print(solution('B',3))

# #for문으로 돌려주고 공백 split로 나누고 z는 기준 나눠준다.
#s1 = list(string.ascii_lowercase)
#s2 = list(string.ascii_uppercase)


# import string

def solution(s,n):
    
    
   
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    
    result = ''
    
        
    for i in s:
        if i in a:
            if (a.index(i)+n<26) :
                
                result += a[a.index(i)+n]
            else  :
                 
                result += a[a.index(i)+n-26]
        elif i in A:
            if (A.index(i)+n<26) :
                
                result += A[A.index(i)+n]
            else :
                
                result += A[A.index(i)+n-26]
        else :
            result +=' '
   

    return result 

print(solution('A F z',5))

# def solution(s,n):
    
#     a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#     A=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
#     s_list = s.split()

    
#     for i in s_list:
#         if (a.index(i)+n<26):
#             return a[a.index(i)+n]
#         else :
#             return a[a.index(i)+n-26]
        
#     for i in s_list:   
#         if (A.index(i)+n<26):
#             return A[A.index(i)+n]
#         else :
#             return A[A.index(i)+n-26]

# print(solution('c d',5))
            





