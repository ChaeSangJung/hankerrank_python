https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    tmp = []
    answer = []
    for i in range(len(arr1)) :
        for j in range(len(arr1[i])) :
            tmp.append(arr1[i][j] + arr2[i][j])
        answer.append(tmp)
        tmp = []
    return answer