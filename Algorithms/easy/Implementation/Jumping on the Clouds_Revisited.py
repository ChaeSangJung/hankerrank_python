https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

n = 9
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

    현재 위치는 n을 벗어 나지 못한다.
    0 2 4 6 8 1 3 5 7 9

    현재위치 + 점프 계수(k)를 %n 해서 나온 값이 현재 위치가 된다.