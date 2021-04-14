https://www.hackerrank.com/challenges/utopian-tree/problem

찬찬히 문제를 읽고 그대로 구현하면 됨

def utopianTree(n):
    height = 1
    for i in range(n):
        if (i%2 == 0):
            height *= 2
        elif (i%2 == 1):            
            height += 1
    return height

def utopianTree(n):
    height = 0
    for i in range(n+1):
        if (i == 0):
            height = 1
        elif (i%2 == 0 and i != 0):
            height += 1
        elif (i%2 == 1):            
            height *= 2
    return height