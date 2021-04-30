https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    # 실제 시험보는 곳에서 time을 라이브러리를 못쓴다면...
    # 2016년 1월 1일은 금요일. 윤년이다(2월29일 있음).
    # a는 달이다. b는 일이다.
    # 1월1일로부터 달력 계산을 위해 빼고 그 차이만큼 date라는 배열에서 인덱싱을 확인하면된다.
    # a는 1~12, b는 1~31
    # 2월1일을 계산하라면 month(2-1=> 1 * 31), day(1-1 => 0)

    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    diff = b-1

    for idx in range(a-1):
        diff += month[idx]

    return date[diff % 7]

def solution(a, b):
    date = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    return days[(sum(months[:a-1])+b-1)%7]