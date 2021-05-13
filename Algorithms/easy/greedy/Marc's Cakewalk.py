https://www.hackerrank.com/challenges/marcs-cakewalk/problem

def marcsCakewalk(calorie):
    # Write your code here
    calorie = sorted(calorie, reverse=True)
    answer = 0
    for index, value in enumerate(calorie):
        answer += 2**index*value

    return answer