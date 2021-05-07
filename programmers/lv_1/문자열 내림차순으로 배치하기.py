https://programmers.co.kr/learn/courses/30/lessons/12917

def solution(s):
    return ''.join([chr(n) for n in sorted([ord(c) for c in list(s)], reverse=True)])

def solution(s):
  temp=[]
  answer=''
  for cha in s:
    temp.append(ord(cha))
  temp.sort(reverse = True)
  for x in temp:
    answer += chr(x)
  return answer