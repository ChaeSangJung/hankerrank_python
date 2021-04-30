https://programmers.co.kr/learn/courses/30/lessons/12947

def Harshad(n):
    # n은 하샤드 수 인가요?
    st = str(n)
    a = 0
    for i in range(len(st)):
        a += int(st[i])

    return True if n%a == 0 else False

def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0