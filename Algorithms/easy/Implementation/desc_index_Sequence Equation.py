https://www.hackerrank.com/challenges/permutation-equation/problem

p=[4, 3, 5, 1, 2]

p.insert(0,0)
output = []

for num in range(0,len(p)):  
  output.append(p.index(p.index(num)))

output.pop(0)

print(output)
# 1,3,5,4,2

x=1
1은 index4에 있고 4는 index"1"에 있지롱~

x=2
2는 index5에 있고 5는 index"3"에 있지롱~

x=3
3은 index2에 있고 2는 index"5"에 있지롱~

x=4
4는 index1에 있고 1은 index"4"에 있지롱~

x=5
5는 index3에 있고 3은 index"2"에 있지롱~

# 위치 반환(index)
index(x) 함수는 리스트에 x 값이 있으면 x의 "위치 값"을 돌려준다.

>>> a = [1,2,3]
>>> a.index(3)
2
>>> a.index(1)
0
위 예에서 리스트 a에 있는 숫자 3의 위치는 a[2]이므로 2를 돌려주고, 숫자 1의 위치는 a[0]이므로 0을 돌려준다.

다음 예에서 값 0은 a 리스트에 존재하지 않기 때문에 값 오류(ValueError)가 발생한다.

>>> a.index(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 0 is not in list