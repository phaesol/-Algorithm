# def solution(d, budget):
#     num_list = []
#     a = sorted(d)
   
#     for i in a:
#         num_list.append(i)
#         if sum(num_list) > budget:
            
#             break
    
#     print(num_list) 
   
    
# solution([2,2,3,4,6],8)

# def solution(d, budget):
#     num_list = []
#     a = sorted(d)
    
#     if sum(d)<= budget:
        
#         return len(d)
#     else:
#         for i in a:
#             num_list.append(i)
#             if  sum(num_list) > budget:
#                 break
#         print(num_list)
#         return len(num_list)-1 
    
    
    
    
        
# print(solution([2,2,3,1],10))

# def solution(d, budget):
#     d.sort()
#     cnt = 0
#     for i in d :
#         budget -= i
#         if budget < 0 :
#                break
#         cnt += 1
#     answer = cnt
    
#     return answer 

# print(solution([2,2,3,1,9],10))

# a = 0
# while (a<10):
#     print(a)
#     a = a+1
#     if a >= 10:
#         break


num = "12345"
string = "abcd"

print(num.isalpha())
print(string.isalpha())


