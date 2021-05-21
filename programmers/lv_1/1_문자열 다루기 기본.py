https://programmers.co.kr/learn/courses/30/lessons/12918

num='111'
fake='hundred'
hanguel='한글'

#isdigit 사용
print(num.isdigit())
print(fake.isdigit())
print(hanguel.isdigit())

print('--------------------------')

#isalpha 사용
print(num.isalpha())
print(fake.isalpha())
print(hanguel.isalpha())

True
False
False

False
False
True

def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit():
        return True
    else:
        return False