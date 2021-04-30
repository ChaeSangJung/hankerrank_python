https://programmers.co.kr/learn/courses/30/lessons/17681

https://docs.python.org/ko/3/library/functions.html#bin
bin()
정수를 《0b》 가 앞에 붙은 이진 문자열로 변환합니다. 결과는 올바른 파이썬 표현식입니다. x 가 파이썬 int 객체가 아니라면, 정수를 돌려주는 __index__() 메서드를 정의해야 합니다. 몇 가지 예를 들면:

>>>
bin(3)
'0b11'
bin(-10)
'-0b1010'
접두어 《0b》 가 필요할 수도, 필요 없을 수도 있다면, 다음 방법의 하나를 사용할 수 있습니다.

>>>
format(14, '#b'), format(14, 'b')
('0b1110', '1110')
f'{14:#b}', f'{14:b}'
('0b1110', '1110')
자세한 내용은 format()을 보세요.

format()
format_spec 의 제어에 따라, value 를 《포맷된》 표현으로 변환합니다. format_spec 의 해석은 value 인자의 형에 의존하지만, 대부분의 내장형에 의해 사용되는 표준 포매팅 문법이 있습니다: 포맷 명세 미니 언어.

기본 format_spec 은 빈 문자열이며 일반적으로 str(value) 를 호출하는 것과 같은 효과를 줍니다.

format(value, format_spec) 에 대한 호출은 type(value).__format__(value, format_spec) 로 번역되는데, value의 __format__() 메서드를 검색할 때 인스턴스 딕셔너리를 건너뜁니다. 메서드 검색이 object 에 도달하고 format_spec 이 비어 있지 않거나, format_spec 또는 반환 값이 문자열이 아닌 경우 TypeError 예외가 발생합니다.

버전 3.4에서 변경: object().__format__(format_spec) 은 format_spec 이 빈 문자열이 아닌 경우 TypeError 를 일으킵니다.

[Python] 2진수, 8진수, 10진수, 16진수 변환
https://brownbears.tistory.com/467

[python] zip 함수
https://www.daleseo.com/python-zip/

마치 옷의 지퍼(zipper)처럼 두 그룹의 데이터를 서로 엮어주는 파이썬의 내장 함수 zip()에 대해서 알아보도록 하겠습니다.

zip
zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 각 객체가 담고 있는 원소를 터플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환합니다. 설명이 좀 어렵게 들릴 수도 있는데요. 간단한 예제를 보면 이해가 쉬우실 겁니다.

>>> numbers = [1, 2, 3]
>>> letters = ["A", "B", "C"]
>>> for pair in zip(numbers, letters):
...     print(pair)
...
(1, 'A')
(2, 'B')
(3, 'C')
위 코드를 보면 numbers 리스트와 letters 리스트를 zip() 함수에 인자로 넘겨서 호출 후에, for 문으로 zip() 함수의 반환값을 대상으로 루프를 돌면서 터플을 차례로 출력하고 있습니다.

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
마치면서
이상으로 파이썬에 내장된 재미있는 함수인 zip()에 대해서 살펴보았습니다.


[python] rjust, ljust, zfill
https://www.crocus.co.kr/1660

https://dojang.io/mod/page/view.php?id=2460
47.1.3  비트 논리 연산자 사용하기
47.1.4  비트 연산자 진리표

def solution(n, arr1, arr2):
    # 포맷을 이용한 진수 변환
    for i in range(n):
        arr1[i]=format(arr1[i],'b')
        arr2[i]=format(arr2[i],'b')

def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):        
        a12 = str(bin(i|j)[2:])        
        a12=a12.rjust(n,'0')
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = str(bin(arr1[i]|arr2[i])[2:]).rjust(n,'0').replace('1','#').replace('0',' ')
        answer.append(a)
    return answer

solution = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])

string.replace() 는 원본 string을 바꿔주는 게 아니다!!
문제를 풀면서 문자열안에 있는 문자를 직접 바꾸고 싶어 s.replace()를 시도했는데 잘 안됐다. s.replace(i, i.upper()) 왜 안되는 거지?.?

찾아보니 replace()는 원본 문자열을 바꿔주는 게 아니라 값을 바꾼 새로운 문자열을 반환하는 함수였다. 즉 s.replace(i, i.upper())를 하면 
s 원본이 아닌 다른 새로운 문자열을 반환하는 것...!!! 그래서 안됐던 거였음

replace() is an inbuilt function in Python programming language that returns a copy of the string 
where all occurrences of a substring are replaced with another substring.

https://www.geeksforgeeks.org/python-string-replace/