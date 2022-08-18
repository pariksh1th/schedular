from user_input import SEC3A
import random


day_1 = ['L', 'l', 'L', 'L']
day_2 = ['L', 'l', 'L', 'L']
day_3 = ['L', 'l', 'L', 'L']
day_4 = ['L', 'l', 'L', 't']
day_5 = ['L', 't', 't', 'L', 't']
code = [0 , 0, 0, 0, 1]
week = [day_1, day_2, day_3, day_4, day_5]
ttCSE3A = []
trL = {}
trT = {}
labA = []
l = []
l1 = []

for _ in SEC3A:
    y = []
    for i in range(int(SEC3A[_][1][0])):
        y.append(SEC3A[_][0] + 'L')
    if len(SEC3A[_]) > 2:
        for i in range(int(SEC3A[_][3][0])):
            y.append(SEC3A[_][2] + 'L')
    trL[_] = y

for _ in SEC3A:
    y = []
    for i in range(int(SEC3A[_][1][2])):
        y.append(SEC3A[_][0] + 'tut')
    if len(SEC3A[_]) > 2:
        for i in range(int(SEC3A[_][3][2])):
            y.append(SEC3A[_][2] + 'tut')
    trT[_] = y

for _ in SEC3A:
    for i in range(int(SEC3A[_][1][4])):
        l.append(SEC3A[_][0] + 'p')
        l1.append(SEC3A[_][0] + 'p')
    if len(SEC3A[_]) > 2:
        for i in range(int(SEC3A[_][1][4])):
            l.append(SEC3A[_][2] + 'p')
            l1.append(SEC3A[_][2] + 'p')

if len(l) == 1:
    l = [l[0], l[0]]
    l1 = [l1[0], l1[0]]
elif len(l) == 2:
    l = [l[0], l[0], l[1], l[1]]
    l1 = [l1[0], l1[0], l1[1], l1[1]]
elif len(l) == 3:
    l = [l[0] + '/' + l[1], l[0] + '/' + l[1], l[2], l[2]]
    l1 = [l1[0] + '/' + l1[1], l1[0] + '/' + l1[1], l1[2], l1[2]]
elif len(l) == 4:
    l = [l[0] + '/' + l[1], l[0] + '/' + l[1], l[2] + '/' + l[3], l[2] + '/' + l[3]]
    l1 = [l1[0] + '/' + l1[1], l1[0] + '/' + l1[1], l1[2] + '/' + l1[3], l1[2] + '/' + l1[3]]

labA = l
labB = l1
labs = len(l)

count = 0
for _ in trL:
    while len(trL[_]) != 0:
        flag = 0
        x = random.randint(0, len(week) - 1)
        while week[x][0] == 'L':
            week[x][0] = trL[_].pop(0)
            flag = 1
        while week[x][2] == 'L' and flag == 0:
            week[x][2] = trL[_].pop(0)
            flag = 1
        while week[x][3] == 'L' and flag == 0:
            week[x][3] = trL[_].pop(0)
        count += 1
    if count > 8:
        break


i = 0
for _ in trL:
    while len(trL[_]) != 0 and i < 5:
        flag = 0
        if week[i][0] == 'L':
            week[i][0] = trL[_].pop(0)
        elif week[i][2] == 'L':
            week[i][2] = trL[_].pop(0)
        elif week[i][3] == 'L':
            week[i][3] = trL[_].pop(0)
        i += 1

while len(labA) != 0:
    x = random.randint(0, len(week) - 1)
    if week[x][1] == 'l':
        y = random.randint(0, len(labA) - 1)
        week[x][1] = labA.pop(y)

for _ in trT:
    while len(trT[_]) != 0:
        if week[4][1] == 't':
            y = random.randint(0, len(trT[_]) - 1)
            week[4][1] = trT[_].pop(y)
        elif week[4][2] == 't':
            y = random.randint(0, len(trT[_]) - 1)
            week[4][2] = trT[_].pop(y)
        else:
            week[3][3] = trT[_].pop(y)

labcode = []
while len(week) != 0:
    x = random.randint(0, len(week) - 1)
    ttCSE3A.append(week[x])
    labcode.append(code[x])
    y = week.pop(x)
    z = code.pop(x)

