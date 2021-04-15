https://www.hackerrank.com/challenges/library-fine/problem

def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0

    if y1 > y2:
        fine = 10000
    elif m1 > m2 and y1 == y2:
        fine = (m1- m2)*500
    elif d1 > d2 and m1 == m2 and y1 == y2:
        fine = (d1- d2)*15

    return fine