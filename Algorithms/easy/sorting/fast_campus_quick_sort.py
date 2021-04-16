def qsort(data):
    if len(data) <= 1:
        return data
    
    left, right = list(), list()
    pivot = data[0]
    
    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])
    
    return qsort(left) + [pivot] + qsort(right)

data_list = [85, 90, 79, 86, 67, 38, 76, 60, 94, 33]

pivot 기준 
pivot보다 작은 것 : left=[]
pivot보다 큰 것  : right=[]

pivot = data[0] 85

for index in range(1, len(data) 10):
    index = 1
    if pivot 85 > data[index 1] 90:
    else :
        right.append(data[index 1] 90) right = ['90']
    index = 2
    if pivot 85 > data[index 2] 79:
            left.append(data[index]) left = ['79']
    index = 3
    if pivot 85 > data[index 3] 86:
    else:
        right.append(data[index 3] 86) right = [90, '86']
    index = 4
        left.append(data[index]) left = [79,'67']
    index = 5
        left.append(data[index]) left = [79,67,'38']
    index = 6
        left.append(data[index]) left = [79,67,38,'76']
    index = 7
        left.append(data[index]) left = [79,67,38,76,'60']
    index = 8
        right.append(data[index]) right = [90, 86,'94']
    index = 9
        left.append(data[index 3] 86) left = [79,67,38,76,60,'33']

[79,67,38,76,60,33] '85' [90,86,94]
[67,38,76,60,33] 79 [] 85 [86] 90 [94]
[38,60,33] 67 [76] 79 [] 85 [86] 90 [94]
[33] 38 [60] 67 [76] 79 [] 85 [86] 90 [94]
