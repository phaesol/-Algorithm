
#효율성 제로
# def solution(participant, completion):
#     answer = ""
#     for i in participant:
#         if participant.count(i)>completion.count(i):
#             answer += i
#             break
            
#     return answer











# def solution(participant, completion):
    
#     answer =""
    
#     for i in participant:
#         if i not in completion:
#             answer+= i
#         elif answer == "" and participant.count(i)>completion.count(i):
#             answer += i
#     # for v in participant:
#     #     if answer == "" and participant.count(v)>1:
#     #         answer+= v
    
#     return answer

# def solution(participant, completion):
    
#     answer =""
    
#     for i in participant:
#         if i not in completion:
#             answer+= i
#         elif answer == "" :
#             if participant.count(i)>completion.count(i):
#                 answer += i

#     return answer


# def solution(participant, completion):
    
#     answer =""
    
#     for i in participant:
        
#         if   participant.count(i)>completion.count(i):
#                 answer+= i
#                 break
   

#     return answer

# def solution(participant, completion):
   
#     a = sorted(participant)
#     b = sorted(completion)
#     print(a)
#     print(b)
#     if a[-1] != b[-1]:
#         return(a[-1])
#     else:
#         return(a[2])
# print(solution(["ha"],[]))


# def solution(participant, completion):
#     a =  sorted(participant)
#     b = sorted(completion)
#     print(a)
#     print(b)
#     if a[-1]!= b[-1]:
#         return a[-1]
#     else:
#         return b[-2]

# print(solution(["a","a","b"],["a","a"]))

# solution["a","a","b","b","c"]"a","b","b","c"
# abc   abc  a
# abc   abc  a

# a=["a","a"]
# b = set(a)
# c = list(b)
# print(c)




# def solution(participant, completion):
#     result =  set(participant)-set(completion)
#     result_list = list(result)
#     print(set(completion))
    
#     if len(set(completion))> 1 and len(set(participant)) >len(set(completion)):
        
#         return ("".join(result_list))
    
#     elif len(set(participant)) == len(set(completion)):
#         a = sorted(participant)
#         print(a)
#         b = a[1:len(participant)-1]
#         print(b)
#         return("".join(set(b)))
    
#     else:
#         for i in participant:
#             if i not in completion:
#                 return i
        
# print(solution(["mislav",'mislav',"mislav","stanko"],["mislav","mislav","mislav"]))

#                     #  'mislav',"stanko","ana"            



# #틀린코드
# def solution(participant, completion):
    
#     a =  sorted(participant)
    
#     b =  sorted (completion)
#     print(a)
#     print(b)
#     for i in range(len(b)):
    
#         if a[i] != b[i]:
            
#             return a[i]
#         else:
#             return a[-1]





    # p =  sorted(participant)
    
    #     c =  sorted (completion)
    #     print(p)
    #     print(c)

    #     if p[-1] != c[-1]:
            
    #         return p[-1]
    
    #     elif p[0] != c[0]:
    #         return p[0]
   
    #     elif  len(p) == 0:
    #         return p[0]
    
    #     else:
            
    #     b = p[1:len(p)-1]
    #         c = set(b)
    #         d = list(c)
    #         return ("".join(d))

# def solution(participant, completion):
        
#         p =  sorted(participant)
    
#         c =  sorted (completion)
#         print (p)
#         print(c)
#         arr = p[1:len(p)-1]
#         arr_1 = c[1:len(c)]
    
      
#         if p[-1] != c[-1]:
            
#             return p[-1]
    
#         elif p[0] != c[0]:
#             return p[0]
   
#         elif  len(c) == 0:
#             return p[0]
    
#         else:
           
#             for i in arr:
#                 if arr[i] != arr_1[i]:
#                     return arr[i]

# print(solution(["leo",'kiki',"eden"],["eden","kiki"]))

            
           
          
          
# print(solution(["a","b","c","d"],["a","b", ""]))


a = [ 1, 2, 2, 3, 3]

b = a.index(2)


print(b)


# print(list(d))


# a = ["h","e","l","l","o"]

# b = ("_".join(a))
# print(b)