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