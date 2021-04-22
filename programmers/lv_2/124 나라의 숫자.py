https://programmers.co.kr/learn/courses/30/lessons/12899

3진수의 개념을 이용해서 변환

def solution(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1 #인덱스떄문에 1을뺴서 0부터 대입
        answer = num[n % 3] + answer
        n //= 3

    return answer

2진수

x = 10
y=""

while x>0:
    y=str(x%2)+y
    x//=2
print(y)

n = 10

while n:10 > 0:
    n -= 1,9
    answer:1 = num[n:9 % 3 ,0] 1 + answer
    n:3 //= 3

    n -= 1 ,2
    answer = num[n:2 % 3,2] 4 + answer 1
    n //= 3