https://www.hackerrank.com/challenges/the-hurdle-race/problem

# Complete the hurdleRace function below.
def hurdleRace(k, height):    
    potion = 0

    height.sort()
    n = len(height)
    if(height[n-1]-k <= 0):
        potion=0
    else:
        potion = height[n-1]-k

    return potion

def hurdleRace(k, height):
    potion = 0
    cnt = 0

    for x in height:
        cnt = x - k
        if cnt > potion:
            potion = cnt
    
    return potion