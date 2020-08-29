#같은 숫자는 싫어.

# def solution(arr):
#     new_list=[]
   
#     for i in range(len(arr)):
#         print(arr[i+1])

            
         
#     return new_list
# solution([4,4,3,3,2,2])


# def solution(arr):
#     new_list=[]
   
#     for i in range(len(arr)):
#         if i == 0 and arr[i] == arr[i+1] :
#             new_list.append(arr[i])
           
#         elif arr[i] != arr[i-1] :
#             new_list.append(arr[i])
      
            
         
#     return new_list
# solution([4,4,3,3,2,2])

a = ['첫번째','두번째','세번째']
b=[]
for i,name in enumerate(a):
    b.append((i,name))
print(b)