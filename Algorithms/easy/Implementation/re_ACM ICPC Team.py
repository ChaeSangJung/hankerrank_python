https://www.hackerrank.com/challenges/acm-icpc-team/problem

def acmTeam(topic):
    cnt = 0
    num_count = 0
    for i in range(len(topic)-1):
        for j in range(i+1, len(topic)):

            num_tmp = bin( int(topic[i],2) | int(topic[j],2)).count("1")

            if num_count < num_tmp:
                num_count = num_tmp
                cnt = 1
            elif num_count == num_tmp:
                cnt +=1


    return (num_count, cnt)