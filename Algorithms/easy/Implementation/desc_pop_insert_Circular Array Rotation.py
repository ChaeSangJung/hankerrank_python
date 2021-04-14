https://www.hackerrank.com/challenges/circular-array-rotation/problem

n=3 
k=2 
q=3

a=[1,2,3]
queries=[2,1,0]

j= len(a)

for x in range(k):
    n=a[j-1]
    a.pop()
    a.insert(0,n)

newList= []

for m in queries:
    newList.append(a[m])

return newList

# 리스트 요소 끄집어내기(pop)
pop()은 리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제한다.

>>> a = [1,2,3]
>>> a.pop()
3
>>> a
[1, 2]
a 리스트 [1, 2, 3]에서 3을 끄집어내고 최종적으로 [1, 2]만 남는 것을 볼 수 있다.

pop(x)는 리스트의 x번째 요소를 돌려주고 그 요소는 삭제한다.

>>> a = [1,2,3]
>>> a.pop(1)
2
>>> a
[1, 3]
a.pop(1)은 a[1]의 값을 끄집어낸다. 다시 a를 출력해 보면 끄집어낸 값이 삭제된 것을 확인할 수 있다.

# 리스트에 요소 삽입(insert)
insert(a, b)는 리스트의 a번째 위치에 b를 삽입하는 함수이다. 파이썬에서는 숫자를 0부터 센다는 것을 반드시 기억하자.

>>> a = [1, 2, 3]
>>> a.insert(0, 4)
>>> a
[4, 1, 2, 3]
위 예는 0번째 자리, 즉 첫 번째 요소(a[0]) 위치에 값 4를 삽입하라는 뜻이다.

>>> a.insert(3, 5)
>>> a
[4, 1, 2, 5, 3]
위 예는 리스트 a의 a[3], 즉 네 번째 요소 위치에 값 5를 삽입하라는 뜻이다.

j = 3

1. 
a=[1,2,3]
n=a[j:3-1] :3
a.pop() : 3
a.insert(0,n:3) : [3,1,2]

2.
a=[3,1,2]
n=a[j:3-1] :2
a.pop() : 2
a.insert(0,n:2) : [2,3,1]

for m in queries:
    newList.append(a[m:2] => 1) : newList = [1]
    newList.append(a[m:1] => 3) : newList = [1,3]
    newList.append(a[m:0] => 2) : newList = [1,3,2]

newList = [1,3,2]