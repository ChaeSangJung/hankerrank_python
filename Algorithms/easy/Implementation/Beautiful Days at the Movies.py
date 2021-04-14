https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

i=20
j=23
k=6

def beautifulDays(i, j, k):
    count=0
    for l in range(i,j+1):
        n = (str(l)[::-1])
        if(abs(l-int(n))%k ==0):
            count+=1
    return count