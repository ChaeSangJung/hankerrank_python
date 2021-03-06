https://programmers.co.kr/learn/courses/30/lessons/42746

문제 지문 파악하기
이 문제는 주어진 입력 numbers를 가지고 가장 큰 수를 만드는 것입니다. 먼저 첫 번째 입력을 볼까요?

numbers = [6, 10, 2]

여기서 우리가 원하는 기준 "큰 수를 만드는 순"으로 정렬을 해주어야 합니다. 이를테면 6, 10 을 비교합시다.

6 > 10 ( "6" + "10" = "610" > "10" + "6" = "106")

우리 정렬 기준에서는 6이 10보다 우선순위가 높습니다. 왜냐하면, 두 숫자를 가지고 만든 숫자 610, 106 중 6을 먼저 이어 붙인 610이 더 크기 때문이지요. 이제 10, 2를 비교해보겠습니다.

10 < 2 ( "10" + 2 = "102" < "2" + "10" = "210")

여기서는 2가 우선순위가 더큽니다. 왜냐하면, 2를 먼저 이어 붙인 210이 10을 먼저 이어붙인 102보다 크기 때문이지요. 그럼 이제 6과 2를 비교해봅시다.

6 > 2 ("6" + "2" = "62" > "2" + "6" = "26")

따라서 우리 방식대로 정렬을 하면, 다음과 같은 결과를 얻을 수 있습니다.

sorted = [6, 2, 10]

이 배열을 문자열로 만들어서 합쳐주면 우리가 원하는 결과를 얻을 수 있습니다.

result = "6210"

어떻게 동작하는지 아시겠지요?

강사님의 알고리즘 풀이
강사님의 경우 위 아이디어보다, 한 단계 더 진보된 알고리즘을 설계합니다. 
바로 "원소는 0 이상 1000 이하의 수"라는 것을 착안한 것인데, 한 번 살펴보겠습니다. 
만약 numbers에 다음과 같이 입력이 되어있다고 가정해봅시다.

numbers = ["3", "33", "34", "35"]

여기서 각 문자열들을 반복해서 무수히 큰 수를 만들고 4자릿수로 자릅니다.

[ "3"("3333"), "33"("3333"), "34"("3434"), "35"("3535") ]

여기서 만들어진 이 문자열들을 기준으로 역순으로 numbers를 정렬해줍니다.

numbers = [ "35"("3535"), "34"("3434"), "33"("3333"), "3"("3333")]

그 후 numbers에 들어있는 문자열들을 합쳐줍니다.

result = "3534333"

우리가 원하는 결과를 얻을 수 있습니다. 와우! 위의 알고리즘을 순서대로 나타내면 다음과 같습니다.

numbers를 문자열로 치환한다.
각 원소를 "무수히 많이 반복하여 길이를 4로 자른 문자열" 기준으로 numbers를 정렬합니다.
문자열을 합쳐줍니다.
이를 파이썬으로 나타내면 코드는 다음과 같습니다.

def solution(numbers):
    numbers = [ str(x) for x in numbers ]
    numbers.sort(key=lambda x: (x*4)[:4], reverse=True)
    answer = "".join(numbers) if numbers[0] != "0" else "0"
    return answer 


def solution(numbers):
    from _functools import cmp_to_key

    # 1. numbers 정수형 -> 문자열 배열 변환
    numbers = [ str(i) for i in numbers ]
    # 2. 두 문자열을 합쳤을 때 더 큰 숫자 순으로 정렬 
    numbers = sorted(numbers, key=cmp_to_key(lambda x, y: int(x+y) - int(y+x)), reverse=True)
    # 3. 문자열 합침
    answer = "".join(numbers)
    return answer if answer[0] != "0" else "0"