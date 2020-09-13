# array=[1,2,3,4]
# i = 1
# j = 1
# k = 1
# commands = array,[i,j,k]
# array_list=commands[0]
# num = commands[1]
# print(array_list)
# print(num)
        
# def solution(array, commands):
   
#     array_list = commands[0]
#     num_list = array_list[2]
#     print(array_list)
#     print(num_list)
#     result_list = array_list[array_list[0]:(array_list[1]+1)]
#     print(result_list)
#     answer = array[result_list]
#     print(answer)
    
# solution([1,5,2,6,3,7,4],([2,5,3],[4,4,1],[1,7,3]))

# def solution(array, commands):
   
#     array_list = commands[0] #리스트가 예제에선 3개이니 거기서 맨처음 리스트를 빼보았다.
#     num_list = array_list[2] #거기에서 k번째 수를 구해야하니 k따로 뺴보기
#     print(array_list)
#     print(num_list)
   
    
# solution([1,5,2,6,3,7,4],([2,5,3],[4,4,1],[1,7,3]))



# def solution(array, commands):
   
#     for num in commands:
#       print(num)
    
        
   
# solution([1,5,2,6,3,7,4],([2,5,3],[4,4,1],[1,7,3]))


def solution(array, commands):
    result=[]
    for num in commands:
        i = num[0]-1
        j = num[1]
        k = num[2]-1
        a_list = array[i:j]
        b_list = sorted(a_list)
        c_list = b_list[k]

    
<<<<<<< HEAD
        print(b_list)
=======
        print(a_list)
>>>>>>> practice
   
solution([1,5,2,6,3,7,4],([2,5,3],[4,4,1],[1,7,3]))