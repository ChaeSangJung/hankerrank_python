https://programmers.co.kr/learn/courses/30/lessons/42747
https://gurumee92.tistory.com/177?category=782306

문제 지문 파악하기
이번에도, 입력을 통해서 문제를 파악해보도록 하겠습니다. 문제의 입력은 이렇습니다.

입렵:
citations = [3, 0, 6, 1, 5]

H-Index는 N편 중 h번 이상, h번 이하 인용된 수를 뜻합니다. 무슨 말인지 살펴보죠. 해당 입력에서 논문는 총 5편이 있죠? 즉, n은 5입니다.

n = 5

이제 n = 0 부터 H-Index를 찾아봅시다. 다음은 각 n에 대해서, H-Index를 만족하는지 여부입니다.

n = 0    
n >= 0 논문 : 5    
n <= 0 논문 : 1    
H-Index 만족 x    

n = 1    
n >= 1 논문 : 4    
n <= 1 논문 : 2    
H-Index 만족 x    

n = 2    
n >= 2 논문 : 4    
n <= 2 논문 : 2    
H-Index 만족 x    

n = 3    
n >= 3 논문 : 3    
n <= 3 논문 : 3    
H-Index 만족 O    

n = 4    
n >= 4 논문 : 2    
n <= 4 논문 : 3    
H-Index 만족 x

즉 여기서 H-Index는 3입니다. 이를 어떻게 구할 수 있을까요? 제가 세운 알고리즘은 다음과 같습니다. 먼저 citations을 오름차순으로 정렬합니다.

citations = [0, 1, 3, 5, 6]
n = 5

이제 0~n까지 순회하면서, H-Index를 n-i로 합니다. 이제 각 i에 대해서 나타나는 상황을 살펴봅시다. 먼저 i=0입니다.

i=0 citation = 0 // citations[i]
h_index = 5 // n - i

이 때, citation이 h_index보다 크거나 같은지 확인해야 합니다. 크거나 같을때, answer에 h_index를 넣고, 반복문을 멈추면 됩니다. 다음은 0 이후, i에 대한 각 상황입니다.

i=1 citation = 1 // citations[i]
h_index = 4 // n - i
citation < h_index

i=2
citation = 3 // citations[i]
h_index = 3 // n - i
citation >= h_index // 멈춤

즉, i=2에서 h_index를 찾을 수 있습니다. 답은 3입니다.

어떻게 이것이 가능할까요? 이유는 "정렬" 때문입니다. 오름차순으로 정렬한 후라고 합시다. 정렬에 의해서 i에 대해서, i 이후에 원소들은 모두 i에 위치하는 원소보다 크다는 것이 만족됩니다. 즉 다음 수식이 항상 만족되지요.

citations[i + 1] > citations[i]

즉 n-i가 citations[i]에 해당하는 수 이상만큼 인용한 논문의 개수가 됩니다. 때문에, citations[i]가 n-i 즉, h_index 보다 크거나 같을 때, 우리가 원하는 답이 나오는 것입니다.

알고리즘 풀이
"문제 지문 파악하기"를 토대로 세운 알고리즘을 순서대로 나열하면 다음과 같습니다.

1. citations을 오름차순으로 정렬합니다.
2. citations 길이 n을 구합니다.
3. 0~n까지 다음을 반복합니다.
    1. hIndex를 구합니다. (hIndex = n-i)
    2. citations[i]가 hIndex 이상이라면, answer에 hIndex를 저장하고 반복을 멈춥니다.
4. answer를 반환합니다.

def solution(citations):
    answer = 0
    # 1. citations을 오름차순으로 정렬합니다.
    citations.sort()
    # 2. citations 길이 n을 구합니다.
    n = len(citations)
    # 3. 0~n까지 다음을 반복합니다
    for i in range(n):
        # 1. hIndex는 n-i입니다.
        hIndex = n-i
        # 2. citations[i]가 hIndex보다 크거나 같으면, answer에 hIndex를 저장하고 반복을 멈춥니다. 
        if citations[i] >= hIndex:
            answer = hIndex
            break
    
    return answer