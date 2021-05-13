https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

from collections import deque

def hackerrankInString(s):
    # Write your code here
    stack = ['h','a','c','k','e','r','r','a','n','k']
    dq=deque(stack)

    answer ='YES'
    
    for word in s:
        if len(dq) != 0 and word == dq[0]:
            dq.popleft()
    if len(dq) != 0 :
        answer = 'NO'
    return answer