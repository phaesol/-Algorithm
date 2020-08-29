def solution(answers):
    # first_list = []
    # second_list =[]
    # third_list = []

    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    first_cnt,second_cnt,third_cnt=0
    
    for i in range(len(answers)):
        if answers[i] == first[i] :
            first_list.append(i)
    for v in range(len(answers)):
        if answers[v] == second[v]:
            second_list.append(v)
    for s in range(len(answers)):
        if answers[s] == third[s]:
             third_list.append(s)

            
    result = [len(first_list),len(second_list),len(third_list)]
    
    target =  max(result)
   
    index_list =[ i for i, x in enumerate( result ) if x == target ]
    result_list=[]
    for f in index_list:
        result_list.append(f+1)

    return result_list


def solution(answers):
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    first_cnt =0
    second_cnt =0
    third_cnt=0
    
    for i in range(len(answers)):
        if answers[i] == first[i] :
            first_cnt +=1
    for v in range(len(answers)):
        if answers[v] == second[v]:
            second_cnt+=1
    for s in range(len(answers)):
        if answers[s] == third[s]:
             third_cnt +=1

    result = [first_cnt,second_cnt,third_cnt]
    
    
    
    for i in range(len(result)):
        
        if max(result)>=result[i]:
            
            return result.index(max(result))
   