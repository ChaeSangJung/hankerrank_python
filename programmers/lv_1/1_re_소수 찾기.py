https://programmers.co.kr/learn/courses/30/lessons/12921

# 에라토스테네스 체
def solution(n):
    arr_ye = [0]*(n+1)
    cnt = 0
    for i in range (2,n+1):
        if arr_ye[i] == 0:
            cnt +=1
        for j in range(i,n+1,i):
            arr_ye[j] = 1
    return cnt


def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)