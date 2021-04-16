https://www.hackerrank.com/challenges/runningtime/problem

def runningTime(arr):
  shift_arr = []
  for i in range(1, len(arr)):
    shift = 0
    temp = arr[i]
    j = i
    while j > 0 and temp < arr[j-1]:
      arr[j] = arr[j-1]
      j-=1
      shift += 1
    arr[j] = temp
    shift_arr.append(shift)
    print(''.join(str(j) for j in arr), shift)
  return sum(shift_arr)

n = 5
arr = [2, 1, 3, 1, 2]
result = runningTime(arr)
print(result)