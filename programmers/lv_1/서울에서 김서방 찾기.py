https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    for index, name in enumerate(seoul):
        if name == "Kim":
            answer = "김서방은 "+str(index)+"에 있다" #index는 int형이므로 str형태로 변환해주어야함
            return answer


def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))