https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

def solution(phoneBook):
    phoneBook.sort(key=lambda x: len(x))
    for a in range(len(phoneBook)):
        for b in range(a+1, len(phoneBook)):
            if phoneBook[b][:len(phoneBook[a])] == phoneBook[a]:
                return False
    return True

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(len(phone_book)-i-1):
            if phone_book[i] in phone_book[j+i+1]:
                return False
    return True


문제 지문 파악하기

이 문제는 전화번호부에 존재하는 번호 중, 다른 전화번호가 접두어인지 판별하는 문제, 
즉 다른 전화번호로 시작하는 전화번호가 있는지, 판별하는 문제입니다. 
정말 쉽게 풀면 전화번호부를 2번 순회하여, 해당 번호와 다른 번호를 비교하는 방법이 있습니다. 
첫 번째 입력을 통해서 찬찬히 살펴보겠습니다.

입력: ["119", "97674223", "1195524421"]

여기서 "119"를 기준으로 "97674223", "1195524421" 순서대로 시작하는 문자열이 있는지 판별합니다.

"119" - "97674223" : 둘 다 서로에게 시작하는 번호로 쓰이지 않음.
"119" - "1195524421" : "1195524421"는 "119"로 시작함

그렇기 때문에 False를 반환하게 됩니다. 이번엔 다른 입력을 살펴보도록 하죠.

여기서 "123"를 기준으로 "456", "789" 순서대로 시작하는 문자열이 있는지 판별합니다.

"123" - "456" : 둘 다 서로에게 시작하는 번호로 쓰이지 않음.
"123" - "789" : 둘 다 서로에게 시작하는 번호로 쓰이지 않음.

이제 "456" 기준으로 "789"와 비교합니다.

"456" - "789" : 둘 다 서로에게 시작하는 번호로 쓰이지 않음.

모든 문자열을 순회했음에도 서로에게 시작하는 번호로 쓰이는 번호를 찾을 수 없습니다. 
그래서 이 입력은 결과가 True를 반환하게 됩니다. 
알고리즘이 어떠헤 동작하는지 아시겠지요? 
이 알고리즘을 토대로 코드를 기술하면 다음과 같습니다.

def solution(phone_book):
    size = len(phone_book)
    
    for i in range(size-1):
        phone = phone_book[i]
        
        for j in range(i+1, size):
            other = phone_book[j]
            
            if phone.startswith(other) or other.startswith(phone):
                return False
        
    return True

문자열중에 특정 문자를 찾고싶거나, 특정문자로 시작하는 문자열, 특정문자로 끝이나는 문자열 등

문자를 찾는 방법에대해 알아보겠습니다.

find(찾을문자, 찾기시작할위치)

>>> s = '가나다라 마바사아 자차카타 파하'
>>> s.find('마')
5
>>> s.find('가')
0
>>> s.find('가',5)
-1
find는 문자열중에 특정문자를 찾고 위치를 반환해준다, 없을경우 -1을 리턴

 

startswith(시작하는문자, 시작지점)

>>> s = '가나다라 마바사아 자차카타 파하'
>>> s.startswith('가')
True
>>> s.startswith('마')
False

>>> s.startswith('마',s.find('마')) #find는 '마' 의 시작지점을 알려줌 : 5
True
>>> s.startswith('마',1)
False
startswith는 문자열이 특정문자로 시작하는지 여부를 알려준다

true나 false 를 반환

 

두번째 인자를 넣음으로써 찾기시작할 지점을 정할수있다.

 

endswith(끝나는문자, 문자열의시작, 문자열의끝)

>>> s = '가나다라 마바사아 자차카타 파하'
>>> s.endswith('마')
False
>>> s.endswith('하')
True

>>> s.endswith('마',0,10)
False
>>> s.endswith('마',0,6)
True
endswith는 문자열이 특정문자로 끝나는지 여부를 알려준다.

true나 false를 반환

 

두번째인자로 문자열의 시작과 세번째인자로 문자열의 끝을 지정할 수 있다.