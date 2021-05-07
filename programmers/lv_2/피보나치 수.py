https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    if n==1 or n==2:
        return 1
    else:
        return solution(n-1) + solution(n-2)


https://richwind.co.kr/3
피보나치(Fibonacci) 수열을 구현하는 7가지 방법 - 파이썬(Python) 피보나치 구현 7선

def solution(n):
    Table = [0 for c in range(n+1)]
    Table[1] = 1
    for i in range(2, n+1):
        Table[i] = (Table[i-1] + Table[i-2]) % 1234567

    return Table[i]