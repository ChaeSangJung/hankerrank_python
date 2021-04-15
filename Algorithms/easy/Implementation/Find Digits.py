https://www.hackerrank.com/challenges/find-digits/problem

def findDigits(n):
    cnt = 0
    for i in list(str(n)):
        if int(i) != 0 and int(n) % int(i) == 0:
            cnt += 1
    return cnt

def findDigits(n):
    for i in x:
        if int(i) != 0 and int(n)%int(i) == 0:
            cnt +=1
    return cnt