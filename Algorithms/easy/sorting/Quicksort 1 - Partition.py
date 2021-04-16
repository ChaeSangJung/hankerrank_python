https://www.hackerrank.com/challenges/quicksort1/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def quickSort(arr):
  if len(arr) <= 1:
    return arr
  
  left, right= list(),list()
  pivot = arr[0]

  for index in range(1, len(arr)):
    if pivot > arr[index]:
      left.append(arr[index])
    else:
      right.append(arr[index])
  
  left.append(pivot)
  sum = left + right

  return sum