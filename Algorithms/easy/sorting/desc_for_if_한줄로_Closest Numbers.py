https://www.hackerrank.com/challenges/closest-numbers/problem

def closestNumbers(arr):
    output = []
    arr = sorted(arr)
    nowmin = 10**9
    
    for ind in range(1, len(arr)):
        diff = abs(arr[ind-1] - arr[ind])
        
        if diff < nowmin:
            output = [(arr[ind-1], arr[ind])]
            nowmin = diff
        elif diff == nowmin:
            output.append((arr[ind-1], arr[ind]))
            
    flat_list = [item for sublist in output for item in sublist]
        
    return flat_list

https://leedakyeong.tistory.com/entry/python-for%EB%AC%B8-if%EB%AC%B8-%ED%95%9C-%EC%A4%84%EB%A1%9C-%EC%BD%94%EB%94%A9%ED%95%98%EA%B8%B0

1. for 문
- 1차원 list의 각 원소를 한 줄로 출력하기
v = list(range(10))
print(v)
[0,1,2,3,4,5,6,7,8,9]

1) 기존
for i in v:
    print(i)
2) 한 줄로
[i for i in v]
[0,1,2,3,4,5,6,7,8,9]

print(''.join(str(i) for i in v))

- 2차원 list의 각 원소를 한 줄로 출력하기
v = [list(range(10)),[10,11,12]]
print(v)
[[0,1,2,3,4,5,6,7,8,9],[10,11,12]]

1) 기존
for i in v:
  for j in i:
    print(j)

2) 한 줄로
[j for i in v for j in i]
[0,1,2,3,4,5,6,7,8,9,10,11,12]

2. if 문

- one condition
1) 기존
if v<5:
    print(0)
2) 한 줄로 방법 1.
v = 3
if v<5 : print(0)
2) 한 줄로 방법 2.
v=3
print(0 if v<5 else 1)

- more than one condition
1) 기존
if v < 5:
    print(0)
elif v < 10:
    print(1)
elif
    print(2)

2) 한 줄로
v = 3
print(0 if v<5 else 1 if v<10 else 2)

3. for문 + if문
if condition에 해당하는 값만 출력하기
v = list(range(10,20))

1) 기존
for i in v:
    if i == 12:
        print(i)
2) 한 줄로
[i for i in v if i ==12]

- for 문에 해당하는 각각의 원소가 if condition에 해당하는지, 아닌지
1) 기존
for i in v:
    if i ==12:
        print(i)
    else:
        print('no')
2) 한 줄로
[i if i==12 else 'no' for i in v]