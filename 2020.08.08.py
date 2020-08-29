def solution(num):
    count = 1
    
    while num != 1:
        if num%2 != 0:
            num =  num*3+1
            
        elif num%2 == 0:
            num = num/2
        
        else:
            continue
        
        if num == 1:
            
            return count
         
        count= count+1
        
        if count >=500:
            return -1 
           
           
print(solution(1))