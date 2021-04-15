https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

def jumpingOnClouds(c):
    c_length = len(c)-1
    chk = 0
    result = 0

    while chk != c_length:
        if chk != c_length-1 and c[chk + 2] == 0:
            chk +=2
            result +=1
        else:
            chk +=1
            result +=1


    return result

    