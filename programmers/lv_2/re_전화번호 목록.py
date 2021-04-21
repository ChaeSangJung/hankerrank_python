https://programmers.co.kr/learn/courses/30/lessons/42577/solution_groups?language=python3

def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer

def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

def solution(phoneBook):
    phoneBook.sort(key=lambda x: len(x))
    for a in range(len(phoneBook)):
        for b in range(a+1, len(phoneBook)):
            if phoneBook[b][:len(phoneBook[a])] == phoneBook[a]:
                return False
    return True

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(len(phone_book)-i-1):
            if phone_book[i] in phone_book[j+i+1]:
                return False
    return True
