https://www.hackerrank.com/challenges/insertionsort2/problem

# 패캠 삽입정렬 어떻게 만들었는지 알아볼 것!!

def insertionSort(n,ar):
    for i in range(1, n):
        temp = ar[i]
        j = i
        while j > 0 and temp < ar[j-1]:
            ar[j] = ar[j-1]
            j -= 1
        ar[j] = temp
        print (' '.join(str(j) for j in ar))

n = 6
arr = [6, 4, 3, 1, 5, 2]
insertionSort(n,arr)

6 4 3 1 5 2

4 6 3 1 5 2
3 4 6 1 5 2
1 3 4 6 5 2
1 3 4 5 6 2
1 2 3 4 5 6

for i in range(1, n):
    i=1 일때
    temp = ar[i:1] 4
    j = i :1
    while j:1 > 0 and temp:4 < ar[j:1-1] 6:
        ar[j:1] = ar[j:1-1] 6 [6,'6',3,1,5,2] 
        j -= 1, j=0
    while j:0 > 0 and temp:4 < ar[j:1-1] 6: False
    ar[j 0] = temp 4 ['4','6',3,1,5,2]
    print(ar) #[4,6,3,1,5,2]

    [4,6,3,1,5,2]
    i=2 일때
    temp = ar[i:2] 3
    j = i :2
    while j:2 > 0 and temp:3 < ar[j:2-1] 6:
        ar[j:2] = ar[j:2-1] 6 [4,6,'6',1,5,2]
        j -= 1 1
    while j:1 > 0 and temp:3 < ar[j:1-1] 4:
        ar[j:1] = ar[j:1-1] 4 [4,'4','6',1,5,2]
        j -= 1 0
    while j:0 > 0 and temp:3 < ar[j:0-1] 2: False
    ar[j :0] = temp 3 ['3',4,6,1,5,2]
    print(ar) [3,4,6,1,5,2]