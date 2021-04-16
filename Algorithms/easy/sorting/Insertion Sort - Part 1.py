https://www.hackerrank.com/challenges/insertionsort1/problem

n=5
ar =[2, 4, 6, 8, 3]

for k in range(0,n-1):
    for i in range(0,n-1):
        if ar[i] > ar[i+1]:
            temp = ar[i+1]
            ar[i+1] = ar[i]
            for j in ar:
                print(j, end=" ")
            ar[i] = temp
            print()
for j in ar:
    print(j, end=" ")

range(0,n-1):    
    k=0
    range(0,n-1): i=0
        if ar[i:0] 2 > ar[i:0+1] 4:
    range(0,n-1): i=1
        if ar[i:1] 4 > ar[i:1+1] 6:
    range(0,n-1): i=2
        if ar[i:2] 6 > ar[i:2+1] 8:
    range(0,n-1): i=3
        if ar[i:3] 8 > ar[i:3+1] 3:
            temp 3 = ar[i:3+1] 3 temp = 3
            ar[i:3+1] = ar[i:3] 8  ar = [2,4,6,8,"8"]
            for j in ar:
                print(j, end=" ") 2 4 6 8 8
            ar[i:3] = temp 3 [2,4,6,"3","8"]

    k=1
    [2,4,6,3,8]
    range(0,n-1): i=0
        if ar[i:0] 2 > ar[i:0+1] 4:
    range(0,n-1): i=1
        if ar[i:1] 4 > ar[i:1+1] 6:
    range(0,n-1): i=2
        if ar[i:2] 6 > ar[i:2+1] 3:
            temp = ar[i:2+1] 3
            ar[i:2+1] = ar[i:2] 6 ar = [2,4,6,'6',8]
            for j in ar:
                print(j, end=" ") 2 4 6 6 8
            ar[i:2] = temp 3 [2, 4, '3', 6, 8]
    
    [2, 4, 3, 6, 8]
    range(0,n-1): i=3
        if ar[i:3] 6 > ar[i:3+1] 8:
    

