https://www.hackerrank.com/challenges/sock-merchant/problem

1. dictionary(딕셔너리)
딕셔너리 타입은 immutable한 키(key)와 mutable한 값(value)으로 맵핑되어 있는 순서가 없는 집합입니다.
일반적인 딕셔너리 타입의 모습입니다. 중괄호로 되어 있고 키와 값이 있습니다.

>>> {"a" : 1, "b":2}
{'a': 1, 'b': 2}
키로는 immutable한 값은 사용할 수 있지만, mutable한 객체는 사용할 수 없습니다.
# immutable 예
>>> a = {1: 5, 2: 3}   # int 사용
>>> a
{1: 5, 2: 3}
>>> a = {(1,5): 5, (3,3): 3} # tuple사용
>>> a
{(1, 5): 5, (3, 3): 3}
>>> a = { 3.6: 5, "abc": 3} # float 사용
>>> a
{3.6: 5, 'abc': 3}
>>> a = { True: 5, "abc": 3} # bool 사용
>>> a
{True: 5, 'abc': 3}

# mutable 예
>>> a = { {1, 3}: 5, {3,5}: 3}     #set 사용 에러
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
>>> a = {[1,3]: 5, [3,5]: 3}     #list 사용 에러
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> a = { {"a":1}: 5, "abc": 3}     #dict 사용 에러
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'dict'
값은 중복될 수 있지만, 키가 중복되면 마지막 값으로 덮어씌워집니다.
>>> {"a" : 1, "a":2}
{'a': 2}

순서가 없기 때문에 인덱스로는 접근할수 없고, 키로 접근 할 수 있습니다.
>>> d = {'abc' : 1, 'def' : 2}
>>> d[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> d['abc']
1
mutable 한 객체이므로 키로 접근하여 값을 변경할 수 있습니다.
>>> d['abc'] = 5
>>> d
{'abc': 5, 'def': 2}
새로운 키와 값을 아래와 같이 추가할 수 있습니다.
>>> d['ghi'] = 999
>>> d
{'abc': 5, 'def': 2, 'ghi': 999}

2. dictionary(딕셔너리) 선언
딕셔너리 선언할때는 빈 중괄호를 사용합니다.(set 중괄호를 이용하지만 빈중괄호로 선언하면 type이 dict가 됩니다.)
딕셔너리로 명시적으로 선언할 수도 있습니다.
>>> e = {}
>>> type(e)
<class 'dict'>
>>> f = dict()
>>> type(f)
<class 'dict'>
dict constructor를 통해서 아래와 같이 바로 키와 값을 할당하며 선언할 수 있습니다.
>>> newdict = dict( alice = 5, bob = 20, tony= 15, suzy = 30)
>>> newdict
{'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}

3. dictionary(딕셔너리) 변환
리스트 속에 리스트나 튜플, 튜플속에 리스트나 튜플의 값을 키와 value를 나란히 입력하면, 아래와 같이 dict로 변형할 수 있습니다.
>>> name_and_ages = [['alice', 5], ['Bob', 13]]
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
>>> name_and_ages = [('alice', 5), ('Bob', 13)]
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
>>> name_and_ages = (('alice', 5), ('Bob', 13))
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}
>>> name_and_ages = (['alice', 5], ['Bob', 13])
>>> dict(name_and_ages)
{'alice': 5, 'Bob': 13}

4. dictionary(딕셔너리) 복사
얕은 복사(shallow copy) 1
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b =a.copy()
>>> b['alice'].append(5)
>>> b
{'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a
{'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
얕은 복사(shallow copy) 2
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b = dict(a)
>>> a
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> id(a)
4334645680
>>> id(b)
4334648920
깊은 복사(deep copy)
>>> import copy
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b = copy.deepcopy(a)
>>> b['alice'].append(5)
>>> b
{'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}

5. dictionary update(딕셔너리 수)
단일 수정은 키로 접근하여 값을 할당하면 됩니다.
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a['alice'] = 5
>>> a
{'alice': 5, 'bob': 20, 'tony': 15, 'suzy': 30}
여러값 수정은 update 메소드를 사용합니다. 키가 없는 값이면 추가됩니다.
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a.update({'bob':99, 'tony':99, 'kim': 30})
>>> a
{'alice': [1, 2, 3], 'bob': 99, 'tony': 99, 'suzy': 30, 'kim': 30}

*6. dictionary(딕셔너리) for문*
for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당됩니다.
순서는 임의적이다.같은 순서를 보장할 수 없다.
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> for key in a:
...     print(key)
... 
alice
bob
tony
suzy
value값으로 for문을 반복하기 위해서는 values() 를 사용해야합니다.
>>> for val in a.values():
...     print(val)
... 
[1, 2, 3]
20
15
30    
key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용합니다.
>>> for key, val in a.items():
...     print("key = {key}, value={value}".format(key=key,value=val))
... 
key = alice, value=[1, 2, 3]
key = bob, value=20
key = tony, value=15
key = suzy, value=30

7. dictionary(딕셔너리) 의 in
dictionary의 in은 키에 한해서 동작합니다.
>>> 'alice' in a
True
>>> 'teacher' in a
False
>>> 'teacher' not in a
True


8. dictionary(딕셔너리)의 요소 삭제
list와 마찬가지로 del키워드를 사용합니다.
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> del a['alice']
>>> a
{'bob': 20, 'tony': 15, 'suzy': 30}

9. dictionary(딕셔너리)를 읽기 쉽게 표현해주는 pprint
pprint모듈로 dictionary를 찍어보자
>>> from pprint import pprint as pp
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30,"dodo": [1,3,5,7], "mario": "pitch"}
>>> print(a)
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30, 'dodo': [1, 3, 5, 7], 'mario': 'pitch'}
>>> pp(a)
{'alice': [1, 2, 3],
 'bob': 20,
 'dodo': [1, 3, 5, 7],
 'mario': 'pitch',
 'suzy': 30,
 'tony': 15}

 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    
    socks = {}
    res = 0
    
    for el in ar:
        if el not in socks.keys(): 
            socks[el] = 1 
        else:
            socks[el] += 1
    
    for key in socks.keys():
        res += socks[key]//2
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

socks = {}
res = 0

for el in ar:
    if el not in socks.keys(): 
        socks[el] = 1 
    else:
        socks[el] += 1

for key in socks.keys():
    res += socks[key]//2

return res

el = 10
10 not in socks.keys():
    socks[10] = 1 # {10:1}

el = 20
20 not in socks.keys():
    socks[20] = 1 # {10:1, 20:1}

el = 20
else 
    socks[20] += 1 # {10:1, 20:2}

el = 10
else 
    socks[10] += 1 # {10:2, 20:2}

el = 10
else 
    socks[20] += 1 # {10:3, 20:2}

el = 30
30 not in socks.keys():
    socks[30] = 1 # {10:1, 20:2, 30:1}

el = 50
50 not in socks.keys():
    socks[50] = 1 # {10:3, 20:2, 30:1, 50:1}

el = 10
else
    socks[50] = 1 # {10:4, 20:2, 30:1, 50:1}
el = 20
else
    socks[20] = 1 # {10:4, 20:3, 30:1, 50:1}

socks = {10:4, 20:3, 30:1, 50:1}

for 10 in socks.keys():
    res:0 += socks[10]//2 : 2

for 20 in socks.keys():
    res:2 += socks[20]//2 : 1

for 30 in socks.keys():
    res:3 += socks{30}//2 : 0

for 50 in socks.keys():
    res:3 += socks{50}//2 : 0