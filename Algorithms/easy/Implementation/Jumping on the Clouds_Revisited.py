https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

n = 8
k = 2
c = [0, 0, 1, 0, 0, 1, 1, 0, 0]

def jumpingOnClouds(c, k):
    n = len(c)
    cur = k % n
    energy = 100 - 1 - c[cur]*2

    while cur !=0:  
        cur = (cur + k)%n #key 현재 위치 
        energy = energy - 1 - c[cur]*2
    
    return energy