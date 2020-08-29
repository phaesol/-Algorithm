#짝수 홀수 구하기
# def is_odd(a):
#     a =1
#     if a%2==0:
#        return("짝수입니다.")
#     else:
#             return("홀수입니다.")

#평균 구하기

# def avg_numbers(*args):   # 입력 개수에 상관없이 사용하기 위해 *args를 사용
#      result = 0
#      for i in args:
#          result += i
#      return result / len(args)
    
# avg_numbers(1,2)

def average(*args):
    result = 0
    for i in args :
        result += i
        return result / len(args)

print(average(1,3,5))



