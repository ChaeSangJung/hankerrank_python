https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    if n < 10:
        return n;
    return (n % 10) + solution(n // 10)

def solution(n):
    answer=0
    while n != 0:
      answer += n%10
      n=n//10
    return answer

# cf
# 수 뒤집기
def reverse(x):
    res=0
    while x>0:
        t=x%10
        # 나머지 값을 10단위 100단위로 순차적으로 올려준다.
        res=res*10+t
        x=x//10
    return res