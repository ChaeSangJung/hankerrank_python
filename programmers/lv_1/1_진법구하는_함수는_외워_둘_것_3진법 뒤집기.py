https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = ''
    while n>0:
      rest = n % 3
      n //= 3
      answer += str(rest)    
    i=0
    sum = 0
    for x in range(len(answer)-1,-1,-1):      
      sum+=int(answer[x])*3**i      
      i+=1
    return sum


def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer


