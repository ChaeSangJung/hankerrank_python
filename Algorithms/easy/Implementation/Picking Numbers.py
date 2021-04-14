https://www.hackerrank.com/challenges/picking-numbers/problem

where the "absolute difference" between any two elements is less than or equal to 1
절댓값 : absolute difference

a= [1,1,2,2,4,4,5,5,5]

a.sort()
cnt = 0
ans = 0
n= len(a)
for i in range(n):
    for j in range(i+1,n):
        if(a[j] - a[i] == 1 or a[j] - a[i] == 0):
            cnt +=1
    if(ans <= cnt):
        ans = cnt + 1 #결과의 길이
        cnt = 0 # count 초기화
    else:
        cnt = 0

print(ans)

i=0 j=1
if(a[j:1]:1 - a[i:0]:1 == 1 or a[j:1]:1 - a[i:0]:1 == 0):
    cnt = 1 [1,1]
i=0 j=2
if(a[j:2]:2 - a[i:0]:1 == 1 or a[j:2]:2 - a[i:0]:1 == 0):
    cnt = 2 [1,x,2]
if(a[j:3]:2 - a[i:0]:1 == 1 or a[j:3]:2 - a[i:0]:1 == 0):
    cnt = 3 [1,x,x,2]
ans([1,x,x,2] 결과의 길이) = cnt + 1
