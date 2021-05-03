https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers): 
    answer = [] 
    answer_temp = [] 
    count01 = 0 
    count02 = 0 
    count03 = 0 
    one = [1,2,3,4,5] 
    two = [2,1,2,3,2,4,2,5] 
    three = [3,3,1,1,2,2,4,4,5,5] 
    
    for i in range(len(answers)): 
        if answers[i] == one[i%len(one)]: 
            count01+=1 
        if answers[i] == two[i%len(two)]: 
            count02+=1 
        if answers[i] == three[i%len(three)]: 
            count03+=1 
        
    answer_temp = [count01, count02, count03] 
    # c={}    
    for person, score in enumerate(answer_temp):
        # c[person] = answer_temp[person] 
        if score == max(answer_temp): 
            answer.append(person+1) 
    # print(c)
    return answer



**enumerate 함수?

리스트가 있는 경우 순서와 리스트의 값을 전달하는 함수 
순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력받아 인덱스 값을 포함하는
enumerate 객체 리턴 
보통 enumerate 함수는 for문과 함께 자주 사용
 

💡 Example

#01
test = [1,2,3]
for index, value in enumerate(test):
	print(index,value)


#02
a = ['name','python', 'type','snake']
c = {}
for i,name in enumerate(a):
    c[i] = a[i]
print(c)
 

💡 Result

#01 결과값 
(0, 1)
(1, 2)
(2, 3)

#02 결과값 
{0: 'name', 1: 'python', 2: 'type', 3: 'snake'}


출처: https://wooaoe.tistory.com/65 [개발개발 울었다]


def solution(answers):
    p = [[1, 2, 3, 4, 5],
         [2, 1, 2, 3, 2, 4, 2, 5],
         [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    s = [0] * len(p)

    for q, a in enumerate(answers):
        for i, v in enumerate(p):
            if a == v[q % len(v)]:
                s[i] += 1
    return [i + 1 for i, v in enumerate(s) if v == max(s)]


# <!--
def answer_type(pattern, length):
    return pattern * (length // len(pattern)) + pattern[:length%len(pattern)]

def check_answer(p, a):
    return [(x==y) for x,y in zip(p,a)].count(True)

def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    ps = [p1,p2,p3]
    anws =  [answer_type(p, len(answers)) for p in ps]
    chks = [check_answer(a, answers) for a in anws]
    return [i+1 for i in range(len(ps)) if chks[i] == max(chks)]
# -->


문제 지문 파악하기
먼저, 문제를 파악해봅시다. 3명의 수포자는 다음 패턴으로 문제를 찍습니다.

// 각 패턴은 다음 배열의 반복입니다.
1번 학생 = [1, 2, 3, 4, 5]
2번 학생 = [2, 1, 2, 3, 2, 4, 2, 5]
3번 학생 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

첫 번째 입력을 살펴봅시다.

입력:
answers = [1, 2, 3, 4, 5]

이 경우, 1번 학생은 5문제 다 맞히게 됩니다.

answers = [1, 2, 3, 4, 5]
1번 학생 = [1, 2, 3, 4, 5]
score = 5 //각 인덱스의 원소가 모두 같다.

2번 학생은 0개를 맞춥니다.

answers = [1, 2, 3, 4, 5]
2번 학생 = [2, 1, 2, 3, 2] // 4, 2, 5]
score = 0
 
3번 학생은 0개를 맞춥니다.

answers = [1, 2, 3, 4, 5]
3번 학생 = [3, 3, 1, 1, 2] // 2, 4, 4, 5, 5]
score = 0

즉 3명의 학생 중 1번 학생이 5문제로, 제일 많이 맞추게 됩니다. 답은 다음과 같습니다.

answer = [1]
 
이번엔 다음 입력이 있다고 합시다.

입력:
answers = [1, 3, 2, 4, 2, 2, 4, 3, 2, 1]
 
이제 1, 2, 3번 학생 패턴대로 했을 때, 각 점수를 파악해봅시다.

answers = [1, 3, 2, 4, 2, 2, 4, 3, 2, 1]
1번 학생 = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5] //부족한 길이만큼 반복
score = 3

answers = [1, 3, 2, 4, 2, 2, 4, 3, 2, 1]
2번 학생 = [2, 1, 2, 3, 2, 4, 2, 5, 2, 1] //, 2, 3, 2, 4, 2, 5 ] 부족한 길이만큼 반복
score = 4

answers = [1, 3, 2, 4, 2, 2, 4, 3, 2, 1]
3번 학생 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
score = 4
 
이제 최대로 맞힌 점수는 4이며, 2번 3번 학생이 이 점수를 얻었습니다. 따라서 답은 이렇게 됩니다.

answer = [2, 3]
 
어떻게 프로그래밍적으로 풀 수 있을까요? 첫 번째 입력이 들어왔다고 가정하고, 문제를 풀어봅시다. 우리는 먼저 각 학생들의 pattern을 저장하는 2차원 배열을 만들어줍니다.

answers = [1, 2, 3, 4, 5]
patterns = [
    [1, 2, 3, 4, 5], //1번 학생 패턴
    [2, 1, 2, 3, 2, 4, 2, 5], //2번 학생 패턴
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] //3번 학생 패턴
]
이제 각 학생들의 점수를 저장하는 배열 scores를 생성해둡니다.

answers = [1, 2, 3, 4, 5]
patterns = [ 
    [1, 2, 3, 4, 5], 
    [2, 1, 2, 3, 2, 4, 2, 5], 
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] 
]
scores = [0, 0, 0]
 
이제 answers를 0부터 answer의 길이까지 다음과 같이 순회합니다.

i = 0
answers[i] = 1

patterns[0][i] = 1
scores[0] = 1

patterns[1][i] = 2
scores[1] = 0

patterns[2][i] = 3
scores[2] = 0
 
이 때, patterns 역시, j에 대해서 0부터 3까지 순회하는 것이죠.

i = 0    answers[i] = 1        
    j = 0    patterns[j][i] = 1            scores[j] = 1        
    j = 1    patterns[j][i] = 2            scores[j] = 0        
    j = 2    patterns[j][i] = 3            scores[j] = 0    

i = 1    
answers[i] = 2        
    j = 0        patterns[j][i] = 2        scores[j] = 2        
    j = 1        patterns[j][i] = 1        scores[j] = 0        
    j = 2        patterns[j][i] = 3        scores[j] = 0    

i = 2    
answers[i] = 3        
    j = 0        patterns[j][i] = 3        scores[j] = 3        
    j = 1        patterns[j][i] = 2        scores[j] = 0        
    j = 2        patterns[j][i] = 1        scores[j] = 0    

i = 3    
answers[i] = 4        
    j = 0        patterns[j][i] = 4        scores[j] = 4        
    j = 1        patterns[j][i] = 3        scores[j] = 0        
    j = 2        patterns[j][i] = 1        scores[j] = 0    

i = 4    
answers[i] = 5        
    j = 0        patterns[j][i] = 5        scores[j] = 5        
    j = 1        patterns[j][i] = 2        scores[j] = 0        
    j = 2        patterns[j][i] = 2        scores[j] = 0

그래서 scores는 다음과 같이 저장됩니다.

scores = [5, 0, 0]

여기서, 최대 점수를 구합니다.

scores = [5, 0, 0]
max_score = 5
 
이제 scores를 0부터 scores의 길이까지 순회하면서, 최대 점수가 같으면, 해당 인덱스+1을 answer에 저장하면 됩니다. 즉 답은 다음과 같아집니다.

answer = [1]

여기서 중요한 것은, 각 패턴은, answers의 길이보다 작을 수 있습니다. 반복해서 순회하기 위해서, patterns를 접근할 때 다음 수식을 쓰세요.

if answers[i] == patterns[j][i % len(patterns[j])]:
    pass

나머지 연산으로, i가 각 패턴의 길이를 넘어가더라도, 다시, 0부터 시작하게 되는 것이죠. 이렇게 하면, 이 문제를 풀 수 있습니다.

알고리즘 풀이
"문제 지문 파악하기"를 토대로 세운 알고리즘을 순서대로 나열하면 다음과 같습니다.

1. 각 패턴을 만듭니다.
2. 3명에 대한 스코어 배열을 만듭니다.
3. i를 0부터 answers의 길이까지 순회합니다.
    1. j를 0부터 patterns를 길이까지 순회합니다.
        1. answer[i]와 patters[j][i% len(patterns[j])]와 같으면, scores[j] 1 올려줍니다.
4. scores에서 최고점을 구합니다.
5. 최고점과 같은 점수를 받은 학생 번호(i+1)를 answer에 서장합니다.

def solution(answers):
    # 1. 각 패턴을 만듭니다.
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    # 2. 3명에 대한 스코어 배열을 만듭니다.
    scores = [0] * 3
    
    # 3. i를 0부터 answers의 길이까지 순회합니다.
    # 3-1. j를 0부터 patterns를 길이까지 순회합니다.
    # 3-1-1. answer[i]와 patters[j][i% len(patterns[j])]와 같으면, scores[j] 1 올려줍니다.
    for i in range(len(answers)):
        for j, pattern in enumerate(patterns):
            if answers[i] == pattern[i % len(pattern)]:
                scores[j] += 1
    
    # 4. scores에서 최고점을 구합니다.
    max_score = max(scores)
    # 5. 최고점과 같은 점수를 받은 학생 번호를 answer에 서장합니다.
    answer = [ i + 1 for (i, x) in enumerate(scores) if x == max_score ]
    return answer