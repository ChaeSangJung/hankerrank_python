https://programmers.co.kr/learn/courses/30/lessons/42888

idDict = {}

def solution(record):
  answer = []
  logList = []
  for e in record:
    dataList = e.split(" ")
    if dataList[0] == "Leave":
      logList.append([dataList[1], "님이 나갔습니다."])
    elif dataList[0] == "Enter":
      idDict[dataList[1]] = dataList[2]
      logList.append([dataList[1], "님이 들어왔습니다."])
    elif dataList[0] == "Change":
      idDict[dataList[1]] = dataList[2]    
  
  for log in logList:
    answer.append(idDict[log[0]] + log[1])
  return answer



record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

# 딕셔너리 입력
# user_list = {}
# user_list[8] = 'x'
# user_list[6] = 'xx'
# print(user_list) #{8: 'x', 6: 'xx'}
# print(user_list[8]) # 'x'

dataList = ['Enter', 'uid1234', 'Muzi']
elif dataList[0] == "Enter":
idDict[dataList[1]]:uid1234 = dataList[2]:Muzi
idDict={'uid1234':'Muzi'}

logList.append([dataList[1]:uid1234, "님이 들어왔습니다."])
logList = [['uid1234', "님이 들어왔습니다."]]]

dataList = ['Enter', 'uid4567', 'Prodo']
elif dataList[0] == "Enter":
idDict[dataList[1]]:uid4567 = dataList[2]:Prodo

idDict={'uid1234':'Muzi', 'uid4567':'Prodo'}

logList.append([dataList[1]:uid4567, "님이 들어왔습니다."])
logList = [
    ['uid1234', "님이 들어왔습니다."], 
    ['uid4567', "님이 들어왔습니다."]
]

dataList = ['Leave', 'uid1234']
if dataList[0] == "Leave":
logList.append([dataList[1]:uid1234, "님이 나갔습니다."])
logList = [
    ['uid1234', "님이 들어왔습니다."], 
    ['uid4567', "님이 들어왔습니다."],
    ['uid1234', "님이 나갔습니다."]
]

dataList = ['Enter', 'uid1234', 'Prodo']
elif dataList[0] == "Enter":
idDict[dataList[1]]:uid1234 = dataList[2]:Prodo

idDict={'uid1234':'Prodo', 'uid4567':'Prodo'}

logList.append([dataList[1]:uid1234, "님이 들어왔습니다."])
logList = [
    ['uid1234', "님이 들어왔습니다."], 
    ['uid4567', "님이 들어왔습니다."],
    ['uid1234', "님이 나갔습니다."],
    ['uid1234', "님이 들어왔습니다."]
]

dataList = ['Change', 'uid4567', 'Ryan']
elif dataList[0] == "Change":
idDict[dataList[1]]:uid4567 = dataList[2]:Ryan
idDict={'uid1234':'Prodo', 'uid4567':'Ryan'}

logList = [
    ['uid1234', "님이 들어왔습니다."], 
    ['uid4567', "님이 들어왔습니다."],
    ['uid1234', "님이 나갔습니다."],
    ['uid1234', "님이 들어왔습니다."]
]

idDict={'uid1234':'Prodo', 'uid4567':'Ryan'}

for log in logList:
    log = ['uid1234', "님이 들어왔습니다."]
    answer.append(idDict[log[0]:uid1234]:Prodo + log[1]:"님이 들어왔습니다.")
    answer = [
        'Prodo님이 들어왔습니다.',
    ]

    log = ['uid4567', "님이 들어왔습니다."]
    answer.append(idDict[log[0]:uid4567]:Ryan + log[1]:님이 들어왔습니다.)
    answer = [
        'Prodo님이 들어왔습니다.',
        'Ryan님이 들어왔습니다.'
    ]

    log = ['uid1234', "님이 나갔습니다."]
    answer.append(idDict[log[0]:uid1234]:Prodo + log[1]:님이 나갔습니다.)
    answer = [
        'Prodo님이 들어왔습니다.',
        'Ryan님이 들어왔습니다.',
        'Prodo님이 나갔습니다.',
    ]

    log = ['uid1234', "님이 들어왔습니다."]
    answer.append(idDict[log[0]:uid1234]:Prodo + log[1]:님이 들어왔습니다.)
    answer = [
        'Prodo님이 들어왔습니다.',
        'Ryan님이 들어왔습니다.',
        'Prodo님이 나갔습니다.',
        'Prodo님이 들어왔습니다.'
    ]