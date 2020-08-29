def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]         #첫번째, 두번째, 세번째 학생들의 답안 패턴 적기
    cnt = [0,0,0]                         # 맞은 정답 개수를 세는 리스트 만들기
    
    for i in range(len(answers)):
        if answers[i] == first[i] :     # 첫번째 학생의 답 i번째가 정답의 i번째와 일치하면 카운트 첫번째 +1 
            cnt[0] +=1
    
        if answers[i] == second[i]:     # 두번째 학생의 답 i번째가 정답의 i번째와 일치하면 카운트 두번째 +1 
            cnt[1] +=1
 
        if answers[i] == third[i]:      # 세번째 학생의 답 i번째가 정답의 i번째와 일치하면 카운트 세번째 +1 
             cnt [2] +=1

    
    
    big = max(cnt)                     # 정답을 맞춘 개수의 최대값
    
    result_list = [i+1 for i, j in enumerate(cnt) if j == big]    # enumerate를 써서 i번째의 j 값을 가져옴. 최대값과 같으면 리스트에 담아줌. 
    
    return result_list          
    
    
print(solution([1,2,3,4,5,1,2]))

# def solution(answers):
#     first = [1,2,3,4,5]
#     second = [2,1,2,3,2,4,2,5]
#     third = [3,3,1,1,2,2,4,4,5,5]
#     cnt = [0,0,0]
    
#     for i in range(len(answers)):
#         if answers[i] == first[i] :
#             cnt[0] +=1
#     for v in range(len(answers)):
#         if answers[v] == second[v]:
#             cnt[1] +=1
#     for s in range(len(answers)):
#         if answers[s] == third[s]:
#              cnt [2] +=1

    
#     big = max(cnt)
     
#     result_list = [i+1 for i, j in enumerate(cnt) if j >= big]
    
#     return result_list


#   result_list = []
    
#     if cnt[0] >= big:
        
#         result_list.append(1)
#     if cnt[1] >= big:
        
#         result_list.append(2)
    
#     if cnt[2] >= big:
        
#         result_list.append(3)
        
#     return result_list




def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    cnt = [0,0,0]
    
    for i in range(len(answers)):
        if answers[i] == first[i % len(first)] :     #각각의 길이에서 나눈 나머지를 적어줌.
            cnt[0] +=1
    
        if answers[i] == second[i % len(second)]:
            cnt[1] +=1
 
        if answers[i] == third[i % len(third)]:
             cnt [2] +=1

    
    
    big = max(cnt)
    
    
    
    
   
    result_list = [i+1 for i, j in enumerate(cnt) if j == big]
    
    return result_list
    
    
print(solution([1,2,3,4,5,1,2]))