https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    # Write your code here
    for i in range(len(s)-1):
        d1 = abs(ord(s[i])-ord(s[i+1]))
        d2 = abs(ord(s[-1-i]) - ord(s[-1-i-1]))
        
        if d1 != d2:
            return 'Not Funny'
    
    return 'Funny'