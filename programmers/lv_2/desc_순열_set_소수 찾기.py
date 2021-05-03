https://programmers.co.kr/learn/courses/30/lessons/42839

참고 : https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%86%8C%EC%88%98-%EC%B0%BE%EA%B8%B0

import math
from itertools import permutations

def is_prime_number(n):
    """소수판별 함수"""
    if n==0 or n==1:                                # 0,1 은 소수가 아님
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):   # sqrt(n)까지만 for문을 돌면서 확인하면 된다. 2부터? 0과 1은 소수가 아니므로
            if n % i == 0:                          # 2~sqrt(num)까지 나누어 떨어지는 숫자가 있으면 소수가 아님
                return False
        
        return True                                 # for문을 다 돌았는데도 False가 아니면 소수

def solution(numbers):
    answer = []
    for i in range(1, len(numbers)+1):              
        arr = list(permutations(numbers, i))        # permutations(순열)을 사용해 i개씩 묶어지는 list 생성
        for j in range(len(arr)):                   # 생성한 list(arr) 길이만큼 for문 실행
            num = int(''.join(map(str,arr[j])))     # list(arr)의 값들은 tuple들로 되어있으모 join(map(str,))을 사용해 join해준다
            if is_prime_number(num):                
                answer.append(num)                  # is_prime_number() 함수가 True일 경우 (= 소수일 경우) num 추가
    
    answer = list(set(answer))                      # 같은 값이 나올 수 있기 때문에 set()을 통해 중복값 제거
    return len(answer)
    

print(solution("17"))       # result : 3
print(solution("011"))      # result : 2


📌 순열과 조합 라이브러리
1. 순열(permutations)
permutations(반복 가능한 객체, n) // n=몇개를 뽑을 것인지

중복을 허용하지 않는다.
순서에 의미가 있다 (= 같은 값이 뽑히더라도 순서가 다르면 다른 경우의 수로 판단)
from itertools import permutations

print(list(permutations([1,2,3,4], 2)))
print(list(permutations([1,2,3,1], 2)))

# result1
# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]

# result2
# [(1, 2), (1, 3), (1, 1), (2, 1), (2, 3), (2, 1), (3, 1), (3, 2), (3, 1), (1, 1), (1, 2), (1, 3)]

2. 중복 순열(product)
product(반복 가능한 객체, repeat=num)

중복을 허용하는 순열
from itertools import product

print(list(product([1,2,3,4], repeat=2)))
print(list(product([1,2,3,1], repeat=2)))

# result1
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]

# result2
# [(1, 1), (1, 2), (1, 3), (1, 1), (2, 1), (2, 2), (2, 3), (2, 1), (3, 1), (3, 2), (3, 3), (3, 1), (1, 1), (1, 2), (1, 3), (1, 1)]

3. 조합(combinations)
combinations(반복 가능한 객체, n) // n=몇개를 뽑을 것인지

중복을 허용하지 않는다.
순서에 의미가 없다 (= 같은 값이 뽑히면 같은 경우의 수로 판단)
from itertools import combinations

print(list(combinations([1,2,3,4], 2)))
print(list(combinations([1,2,3,1], 2)))

# result1
# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# result2
# [(1, 2), (1, 3), (1, 1), (2, 3), (2, 1), (3, 1)]

4. 중복 조합(combinations_with_replacement)
combinations_with_replacement(반복 가능한 객체, n) // n=몇개를 뽑을 것인지

중복을 허용하는 조합
from itertools import combinations_with_replacement

print(list(combinations_with_replacement([1,2,3,4], 2)))
print(list(combinations_with_replacement([1,2,3,1], 2)))

# result1
# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]

# result2
# [(1, 1), (1, 2), (1, 3), (1, 1), (2, 1), (2, 2), (2, 3), (2, 1), (3, 1), (3, 2), (3, 3), (3, 

3. 셋(set)

     • 셋은 순서가 없는 중복이 불가능한 collection 자료형이다. -> 내장모듈 collections 알아두면 좋음

     • mutable(가변성) 함

     • 요소들 간의 순서가 없음 -> 따라서, indexing이 불가 -> not iterable

     • 중복제거 교집합, 합집합, 차집합 등의 수학적인 계산이 가능

     • 셋은 add(요소 1개 추가), update(여러요소 추가), remove 메소드를 활용하여 요소를 추가/삭제한다.

     • 합집합은 a | b로 표현, 차집합은 a - b로 표현, 교집합은 a & b로 표현


numbers ='013'
answer = []

for i in range(1, len(numbers):3+1 4):
    i=1
    arr = list(permutations(numbers:013, i:1))
        arr = [('0',), ('1',), ('3',)]
        for j in range(len(arr) 3):
            j=0
            num = int(''.join(map(str,arr[j:0])))
            num = 0
            if is_prime_number(num:0):
                is_prime_number(n:0):
                    if n==0 or n==1:                                # 0,1 은 소수가 아님
                    return False
            j=1
            num = int(''.join(map(str,arr[j:1])))
            num = 1
            if is_prime_number(num:1):
                is_prime_number(n:1):
                    if n==0 or n==1:                                # 0,1 은 소수가 아님
                    return False
            j=2
            num = int(''.join(map(str,arr[j:2])))
            num = 3
            if is_prime_number(num:3):
                is_prime_number(n:3):
                for i in range(2, int(math.sqrt(n:3)1.xxxx) + 1 : 2):
                    i = 2
                    if n :3  % i:2 == 0:
                return True
                
                answer.append(num : 3) answer = [3]

    i=2
    arr = list(permutations(numbers:013, i:2))
        arr = [('0', '1'), ('0', '3'), ('1', '0'), ('1', '3'), ('3', '0'), ('3', '1')]
        for j in range(len(arr) 6):
            j=0
            num = int(''.join(map(str,arr[j:0])))
            num = 1
            if is_prime_number(num:1): false

            j=1
            num = int(''.join(map(str,arr[j:1])))
            num = 3
            for i in range(2, int(math.sqrt(n:3)) + 1): true
        .
        .
        .

    i=3
    .
    .
    .


