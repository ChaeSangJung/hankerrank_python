https://www.hackerrank.com/challenges/countingsort2/problem?h_r=next-challenge&h_v=zen

def countingSort(arr):
    cnt = [0] * (max(arr) + 1)
    output = [0] * (len(arr))
    
    for el in arr:
        cnt[el] += 1
        
    total = 0
    for ind in range(len(cnt)):
        old = cnt[ind]
        cnt[ind] = total
        total += old
        
    for el in arr:
        output[cnt[el]] = el
        cnt[el] += 1
        
    return output

# 1.
arr = [4, 3, 6, 5, 7, 9, 8]

cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
output = [0, 0, 0, 0, 0, 0, 0]

cnt = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

total = 0
for ind in range(len(cnt) 10):
    ind = 0
    old 0 = cnt[ind:0]
    cnt[ind :0] = total 0 ,cnt=[0]
    total 0 += old 0

    ind = 1
    old 0 = cnt[ind :1]
    cnt[ind: 1] = total 0, cnt=[0,0]
    total 0 += old 0

    ind = 2
    old 0 = cnt[ind :2]
    cnt[ind :2] = total 0, cnt=[0,0,0]
    total += old

    ind = 3
    old 1 = cnt[ind :3]
    cnt[ind :3] = total 0, cnt=[0,0,0,0]
    total 1 += old 1

    ind = 4 
    old 1 = cnt[ind:4]
    cnt[ind:4] = total 1, cnt=[0,0,0,0,1]
    total 2 += old 1

    ind = 5
    old 1 = cnt[ind : 5]
    cnt[ind:5] = total 2, cnt=[0,0,0,0,1,2]
    total 3 += old 1

    ind = 6
    old 1 = cnt[ind:6]
    cnt[ind : 6] = total 3, cnt=[0,0,0,0,1,2,3]
    total 4 += old 1

    .
    .
    .

    ind = 9
    old:1 = cnt[ind:9]
    cnt[ind:9] = total 6 , cnt=[0,0,0,0,1,2,3,4,5,6]
    total 7 += old 1

    cnt = [0,0,0,0,1,2,3,4,5,6]
output = [0, 0, 0, 0, 0, 0, 0]
arr = [4, 3, 6, 5, 7, 9, 8]

for el in arr:
    el = 4
    output[cnt[el 4] 1] = el 4, output = [0,'4', 0, 0, 0, 0, 0]
    cnt[el 4] += 1, cnt = [0,0,0,0,'2',2,3,4,5,6]

    el = 3
    output[cnt[el 3] 0] = el 3, output = ['3',4, 0, 0, 0, 0, 0]
    cnt[el 3] += 1, cnt = [0,0,0,'1',2,2,3,4,5,6]

    el = 6
    output[cnt[el 6] 3] = el 6, output = [3,4, 0,'6', 0, 0, 0]
    cnt[el 6] += 1, cnt = [0,0,0,1,2,2,'4',4,5,6]

    el = 5
    output[cnt[el 5] 2] = el 5, output = [3,4,'5',6, 0, 0, 0]
    cnt[el 5] += 1, cnt = [0,0,0,1,2,'3',4,4,5,6]

    el = 7
    output[cnt[el 7] 4] = el 7, output = [3,4,5,6,'7', 0, 0]
    cnt[el 7] += 1, cnt = [0,0,0,1,2,3,4,'5',5,6]

    el = 9
    output[cnt[el 9] 6] = el 6, output = [3,4,5,6,7,0,'9']
    cnt[el 9] += 1, cnt = [0,0,0,1,2,3,4,5,5,'7']

    el = 8
    output[cnt[el 8]] = el 8, output = [3,4,5,6,7,'8',9]
    cnt[el 8] += 1, cnt = [0,0,0,1,2,3,4,5,'6',7]

# 2.
arr = [4, 3, 6, 3, 7, 7]

cnt = [0, 0, 0, 0, 0, 0, 0, 0]
output = [0, 0, 0, 0, 0, 0]

cnt = [0, 0, 0, 2, 1, 0, 1, 2]
total = 0

for ind in range(len(cnt) 8):
    ind = 0
    old 0 = cnt[ind : 0]
    cnt[ind : 0] = total 0, cnt = [0]
    total 0 += old 0

    ind = 1
    old 0 = cnt[ind : 1]
    cnt[ind: 1] = total 0 ,cnt = [0,0]
    total 0 += old 0

    ind = 2
    old 0 = cnt[ind :2]
    cnt[ind 2] = total 0, cnt=[0,0,0]
    total 0 += old 0

    ind = 3
    old 2 = cnt[ind :3]
    cnt[ind : 3] = total 0, cnt=[0,0,0,0]
    total 2 += old 2

    ind = 4
    old 1 = cnt[ind : 4]
    cnt[ind : 4] = total 2, cnt = [0,0,0,0,2]
    total 3 += old 1

    ind = 5
    old 0 = cnt[ind : 5]
    cnt[ind : 5] = total 3, cnt = [0,0,0,0,2,3]
    total 3 += old 0

    ind = 6
    old 1 = cnt[ind 6]
    cnt[ind : 6] = total 3, cnt = [0,0,0,0,2,3,3]
    total 4 += old 1

    ind = 7
    old 2 = cnt[ind 7]
    cnt[ind 7] = total 4, cnt = [0,0,0,0,2,3,3,4]
    total 6 += old 2

    cnt = [0,0,0,0,2,3,3,4]
    output = [0, 0, 0, 0, 0, 0]
    arr = [4, 3, 6, 3, 7, 7]

    for el in arr:
        el = 4
        output[cnt[el 4] 2] = el 4, output = [0, 0, '4', 0, 0, 0]
        cnt[el 4] += 1, cnt = [0,0,0,0,'3',3,3,4]

        el = 3
        output[cnt[el 3] 0] = el 3, output = ['3', 0, 4, 0, 0, 0]
        cnt[el 3] += 1, cnt = [0,0,0,'1',3,3,3,4]

        el = 6
        output[cnt[el 6] 3] = el 6, output = [3, 0, 4, '6', 0, 0]
        cnt[el 6] += 1, cnt = [0,0,0,1,3,3,'4',4]

        el = 3
        output[cnt[el 3] 1] = el 3, output = [3, '3', 4, 6, 0, 0]
        cnt[el 3] += 1, cnt = [0,0,0,'2',3,3,4,4]

        el = 7
        output[cnt[el 7] 4] = el 7, output = [3, 3, 4, 6, '7', 0]
        cnt[el 7] += 1, cnt = [0,0,0,2,3,3,4,'5']

        el = 7
        output[cnt[el 7] 5] = el 7, output = [3, 3, 4, 6, 7, '7']
        cnt[el 7] += 1, cnt = [0,0,0,2,3,3,4,'6']