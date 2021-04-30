https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):    
    N = [i for i in range(1,n+1) if n%i==0]
    M = [i for i in range(1,m+1) if m%i==0]

    Max = max([i for i in N if i in M])
    Min = Max*(n/Max)*(m/Max)
    answer = [Max, Min]
    return answer