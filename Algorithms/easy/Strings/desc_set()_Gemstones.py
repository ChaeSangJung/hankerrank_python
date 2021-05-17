https://www.hackerrank.com/challenges/gem-stones/problem

def gemstones(arrays):
    # Write your code here
    superset = set(arrays[0])
    
    for arr in arrays[1:]:
        superset &= set(arr)
        # superset = superset & set(arr)
    
    return len(superset)

set()
중복을 허용하지 않는다.
순서가 없다(Unordered).

>>> s2 = set("Hello")
>>> s2
{'e', 'H', 'l', 'o'}

>>> s1 = set([1, 2, 3, 4, 5, 6])
>>> s2 = set([4, 5, 6, 7, 8, 9])
1. 교집합

s1과 s2의 교집합을 구해 보자.

>>> s1 & s2
{4, 5, 6}
"&" 기호를 이용하면 교집합을 간단히 구할 수 있다.

또는 다음과 같이 intersection 함수를 사용해도 동일한 결과를 돌려준다.

>>> s1.intersection(s2)
{4, 5, 6}
s2.intersection(s1)을 사용해도 결과는 같다.

2. 합집합

합집합은 다음과 같이 구할 수 있다. 이때 4, 5, 6처럼 중복해서 포함된 값은 한 개씩만 표현된다.

>>> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}
"|" 기호를 사용한 방법이다.

>>> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
또는 union 함수를 사용하면 된다. 교집합에서 사용한 intersection 함수와 마찬가지로 s2.union(s1)을 사용해도 동일한 결과를 돌려준다.

3. 차집합

차집합은 다음과 같이 구할 수 있다.

>>> s1 - s2
{1, 2, 3}
>>> s2 - s1
{8, 9, 7}
빼기(-) 기호를 사용한 방법이다.

>>> s1.difference(s2)
{1, 2, 3}
>>> s2.difference(s1)
{8, 9, 7}
difference 함수를 사용해도 차집합을 구할 수 있다.