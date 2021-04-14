https://www.hackerrank.com/challenges/save-the-prisoner/problem

def saveThePrisoner(n, m, s):
    if((m%n+s-1)%n == 0):
        return n
    else:
        return (m%n+s-1)%n