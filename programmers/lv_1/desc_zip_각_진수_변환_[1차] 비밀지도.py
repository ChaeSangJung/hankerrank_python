https://programmers.co.kr/learn/courses/30/lessons/17681


[Python] 2진수, 8진수, 10진수, 16진수 변환
https://brownbears.tistory.com/467

[python] zip 함수
https://www.daleseo.com/python-zip/

[python] rjust, ljust, zfill
https://www.crocus.co.kr/1660

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