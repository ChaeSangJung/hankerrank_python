https://programmers.co.kr/learn/courses/30/lessons/17687

t=4 '튜브가 말해야 하는 숫자의 갯수 숫자 4까지가 아니라.'

def solution(n, t, m, p):
    answer = ''
    length = m * t
    candidate = '0'
    num = 0
    alpha = 'ABCDEF'
    
    while len(candidate) < length: #length 길이보다 작을 때 까지 n진법으로 변환!
        res = ''
        number = num
        while True: # 자연수 number를 n진법으로 변환하는 반복문 
            if number == 0: # 더 이상 나누지 못하면 break
                break
            if number % n:
                if number % n >= 10: # 10~15값이면 alpha와 매핑
                    res += alpha[(number%n) % 10]
                else: # 나머지 값을 res에 담는다.
                    res += str(number % n)                    
            else:
                res += '0'
            number //= n
        num += 1
        candidate += res[::-1] # 역순으로 담았기 때문에 슬라이싱([::-1])을 이용하여 candidate에 담는다.
    for i in range(p-1, length, m):
        answer += candidate[i] # 튜브의 순서에 해당하는 숫자를 answer에 담는다!
    return answer


def solution(n, t, m, p):
    a="0"
    i=0
    #for i in range(t*m):
    while True:
        if len(a)>=t*m:
            break
        b=""
        j=i
        while (j):
            if j%n>9:
                b=big[j%n-10]+b
            else:
                b=str(j%n)+b
            j=j//n
        a=a+b
        i=i+1
    answer = a[p-1::m][:t]
    return answer