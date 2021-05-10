https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n): 
    s = list(s) 
    for i in range(len(s)): 
        if s[i].isupper(): 
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A')) 
        elif s[i].islower(): 
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a')) 
    return "".join(s)


각 문자열을 하나씩 쪼개서 아스키코드로 변환해야하기 때문에 list(s)로 치환해서 담았다. 
만약 s[i]번째 문자가 대문자/소문자라면(isupper/islower) s[i]의 값은 (s[i]의 ASCII값 - 'A'/'a'의 ASCII값(97/65))+n을 해주어 
몇 번째에 있는 알파벳인지 찾아준다. (알파벳은 총 25글자)
ord(s[i])-ord('A') (또는 ord('a')) 26으로 나눈 나머지 값에 'A'/'a' ASCII 값 = 97/65을 더해주면 n만큼 민 값이 나오게 된다. 
%26을 해주는 이유 ? z 또는 Z의 범위를 넘어가지 않도록 하기 위해
즉, 맨 처음 값인 ord('A')와 ord('a')에서 n만큼 증가한 값이 무엇인지 찾는 것이다. 
공백은 밀어도 공백이기 때문에 무시한다.
""을 기준으로 join하여 return


ord('A') : 65
chr(65) : A