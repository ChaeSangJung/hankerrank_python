https://www.hackerrank.com/challenges/angry-professor/problem

def angryProfessor(k, a):
    cnt = 0
    ans=""
    for x in a:
        if(x <=0):
           cnt +=1
    
    if(cnt >= k):
        ans = "NO"
    else:
        ans = "YES"
    
    cnt = 0
    
    return ans