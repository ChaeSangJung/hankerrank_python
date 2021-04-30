https://programmers.co.kr/learn/courses/30/lessons/76501

zip : https://www.daleseo.com/python-zip/

def solution(absolutes, signs):
    answer=0
    for absolute,sign in zip(absolutes,signs):
        if sign:
            answer+=absolute
        else:
            answer-=absolute
    return answer

마치 옷의 지퍼(zipper)처럼 두 그룹의 데이터를 서로 엮어주는 파이썬의 내장 함수 zip()에 대해서 알아보도록 하겠습니다.

zip
zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환합니다. 
설명이 좀 어렵게 들릴 수도 있는데요. 간단한 예제를 보면 이해가 쉬우실 겁니다.

>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
위 코드를 보면 numbers 리스트와 letters 리스트를 zip() 함수에 인자로 넘겨서 호출 후에, 
for 문으로 zip() 함수의 반환값을 대상으로 루프를 돌면서 터플을 차례로 출력하고 있습니다.

zip() 함수를 사용하지 않고, 인덱스(index) 변수를 사용해서 위 코드를 다시 작성해보면 좀 더 이해가 쉬우실 겁니다.

>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for i in range(3):
...     pair = (numbers[i], letters[i])
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
위와 같이 zip() 함수를 사용하면 마치 옷의 지퍼를 올리는 것 처럼 양 측에 있는 데이터를 하나씩 차례로 짝을 지어줍니다.

자 이제, zip() 함수가 기본적으로 어떻게 동작하는지 이해를 하셨다면, 어떤 상황에서 유용하게 사용될 수 있는지 한 번 알아볼까요?

병렬 처리
zip() 함수를 활용하면 여러 그룹의 데이터를 루프를 한 번만 돌면서 처리할 수 있는데요. 가변 인자를 받기 때문에 2개 이상의 인자를 넘겨서 병렬 처리를 할 수 있습니다.

예를 들어, 아래 코드는 3개의 문자열 내의 글자를 하니씩 병렬해서 출력하고 있습니다.

>>> for number, upper, lower in zip("12345", "ABCDE", "abcde"):
...     print(number, upper, lower)
...
1 A a
2 B b
3 C c
4 D d
5 E e
튜플의 원소를 3개의 변수에 할당하기 위해서 for 문에서 인자 풀기(unpacking)를 해주었습니다.

unzip
zip() 함수로 엮어 놓은 데이터를 다시 해체(unzip)하고 싶을 때도 zip() 함수를 사용할 수 있습니다.

먼저 zip() 함수로 2개의 터플의 데이터를 엮은 후 리스트로 변환해보겠습니다.

>>> numbers = (1, 2, 3)
>>> letters = ("A", "B", "C")
>>> pairs = list(zip(numbers, letters))
>>> pairs
[(1, 'A'), (2, 'B'), (3, 'C')]
이 리스트 앞에 풀기(unpacking) 연산자 붙여서 다시 zip() 함수에 넘기면 다시 원래의 2개의 터플을 얻을 수 있습니다.

>>> numbers, letters = zip(*pairs)
>>> numbers
(1, 2, 3)
>>> letters
('A', 'B', 'C')
사전 변환
zip() 함수를 이용하면 두 개의 리스트나 터플 부터 쉽게 사전(dictionary)을 만들 수 있습니다. 키를 담고 있는 리스트와 값을 담고 있는 리스트를 zip() 함수에 넘긴 후, 그 결과를 다시 dict() 함수에 넘기면 됩니다.

>>> keys = [1, 2, 3]
>>> values = ["A", "B", "C"]
>>> dict(zip(keys, values))
{1: 'A', 2: 'B', 3: 'C'}
dict() 함수에 키와 값으로 이루어진 터플을 넘기면 사전이 생성되는 원리를 이용하는 것입니다.

다른 예로, 날짜 데이터의 필드 이름 리스트와 필드 값 리스트를 사전으로 변환해보겠습니다.

>>> dict(zip(["year", "month", "date"], [2001, 1, 31]))
{'year': 2001, 'month': 1, 'date': 31}
주의 사항
zip() 함수로 넘기는 인자의 길이가 다를 때는 주의를 해야 합니다. 왜냐하면 가장 짧은 인자를 기준으로 데이터가 엮이고, 나머지는 버려지기 때문입니다.

>>> numbers = ["1", "2", "3"]
>>> letters = ["A"]
>>> list(zip(numbers, letters))
[('1', 'A')]