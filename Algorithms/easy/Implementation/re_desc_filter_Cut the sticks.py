https://www.hackerrank.com/challenges/cut-the-sticks/problem

arr=[5,4,4,2,2,8]

arr.sort()
new_s = []

while arr:
  cut = arr[0]  
  new_s.append(len(s))
  for i in range(len(s)):
    if arr[i] >= cut:
      arr[i] = arr[i] - cut
  
  arr = list(filter(lambda x: x>0, arr))
print(new_s)

# filter map에 대해 정리!!