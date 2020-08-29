


# def solution(arr, divisor):
#     result = []
   
#     for i in range(len(arr)): #range 함수는 정수만 받아 길이 함수 len 사용
#         if i % divisor == 0:
#             result +=[i]
#         elif i % divisor != 0 :
#             continue
#         elif all(i% divisor!= 0):
#             result +=[-1]
#         else:
#             pass
        
#         return result.sort()
# print(solution([5,9,7,10],5))


# def solution(arr, divisor):
#     result = []
   
#     for i in range(len(arr)):
#         if i % divisor == 0:
#             result.append(i)
#         elif i % divisor != 0 :
#             continue
#         elif all(i% divisor!= 0):
#             result +=[-1]
#         else:
#             pass
        
#         return result.sort() #이렇게 적어주면 none값이 뜨니까 위에다가 result.sort()해주고 다시 리턴해야함


# def solution(arr):
#     # result = []
    
#     for i in arr:
#         print(i)
# solution([1,2,3]) #여기다가 print적어주면 return해주는 값이 없으니까 none뜸 우리 그때 배웟던 것처럼 print 내장해주니까 굳이 print 해줄필요 없음.


# a=["@,@,@,@,@"]

# for i in a:
   
#    print(i)
 
#  def solution(arr, divisor):
    
#     result = []
    
    
#     for i in arr:
#         if i % divisor == 0:
#             result.append(i)
        
#         elif i % divisor!=0:
#               continue
   
#         elif all(i % divisor!=0) :
#             result.append(-1)
    
    
#     return sorted(result)

def solution(arr, divisor):

    result = []


    for i in arr:
        if i % divisor == 0:
            result.append(i)
        else:
            pass

    if result == []:
        result = [-1]


    return sorted(result)
