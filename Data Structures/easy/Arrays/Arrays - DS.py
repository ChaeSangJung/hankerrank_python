https://www.hackerrank.com/challenges/arrays-ds/problem

def reverseArray(a):
  for i in range((len(a)+1)//2):
    a[i],a[-1-i] = a[-1-i],a[i]
  return a