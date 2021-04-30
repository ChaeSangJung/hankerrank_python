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