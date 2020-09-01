#자릿수 더하기
def solution(n):
    answer = []
    n = str(n)  # 숫자는 반복이 불가능하므로 반복가능한 문자열로 변경
    for i in n:
        answer.append(int(i))       #  for문으로 분리 후 다시 int 를 사용해 숫자로 담아줌.
    result=sum(answer)              # 리스트 요소들을 더하는 sum 사용으로 각 자리의 숫자를 더해줌.
    return result         



