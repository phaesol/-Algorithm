# a=1
# b_list = []
# while (a<=1000):
   
#     if a%3==0:
#         b_list.append(a)
#     a=a+1
# print(sum(b_list)) 3의 배수의 합


a=1
b=0
while (a<=1000):
   
    if a%3==0:
        b = b+a
    a=a+1
print(b)