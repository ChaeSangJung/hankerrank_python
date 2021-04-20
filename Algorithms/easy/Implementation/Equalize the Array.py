https://www.hackerrank.com/challenges/equality-in-a-array/problem

def equalizeArray(arr):
    chk_arr = [0]*(max(arr)+1)
    chk_max = 0
    result = 0

    for x in arr:
        chk_arr[x] += 1

    for i in range(len(chk_arr)):
        if chk_max <= chk_arr[i]:
            chk_max = chk_arr[i]

    result = len(arr) - chk_max

    return result

n=8
arr=[1, 2, 3, 1, 2, 3, 3, 3]

chk_arr = [0,0,0,0]
chk_max = 0
result = 0

arr=[1, 2, 3, 1, 2, 3, 3, 3]

for x in arr:
    x= 1
    chk_arr[x:1] += 1 chk_arr = [0,'1',0,0]
    x= 2
    chk_arr[x:2] += 1 chk_arr = [0,1,'1',0]
    x= 3
    chk_arr[x:3] += 1 chk_arr = [0,1,1,'1']
    x= 1
    chk_arr[x:1] += 1 chk_arr = [0,'2',1,1]
    x= 2
    chk_arr[x:2] += 1 chk_arr = [0,2,'2',1]
    x= 3
    chk_arr[x:3] += 1 chk_arr = [0,2,2,'2']
    x= 3
    chk_arr[x:3] += 1 chk_arr = [0,2,2,'3']
    x= 3
    chk_arr[x:3] += 1 chk_arr = [0,2,2,'4']

for i in range(len(chk_arr):4):
    i=0
    if chk_max:0 <= chk_arr[i:0, 0]:
        chk_max:0 = chk_arr[i:0,0]
    i=1
    if chk_max 0 <= chk_arr[i:1 2]:
            chk_max 2 = chk_arr[i]
    i=2
    if chk_max 2 <= chk_arr[i:2 2]:
            chk_max 2 = chk_arr[i]
    i=3
    if chk_max 2 <= chk_arr[i:3 4]:
            chk_max 4 = chk_arr[i]

result 4 = len(arr) 8 - chk_max 4