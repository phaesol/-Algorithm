# def solution(s):
    
#     upper_list = []
#     lower_list=[]
#     for i in s:
#         if i.isupper():
#             upper_list += i
#         else:
#             lower_list += i
#     upper_reverse = reversed(upper_list)
#     lower_reverse = reversed(lower_list)
#     answer = "".join(lower_reverse) + "".join(upper_reverse)
#     return answer

# print(solution("aVsAef"))

a="AZeaa"
b = list(a)
c= sorted(b)
upper=""
lower=""
for i in c:
    if i.isupper():
        upper+= i
    else:
        lower += i
answer = list(reversed(lower))+list(reversed(upper))
print("".join(answer))