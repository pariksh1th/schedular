from user_input import SEC3B
from teachers import teachers
from Sem3CSEA import ttCSE3A, labB
import random

day_1 = ['L', 'l', 'L', 'L']
day_2 = ['L', 'l', 'L', 'L']
day_3 = ['L', 'l', 'L', 'L']
day_4 = ['L', 'l', 'L', 't']
day_5 = ['L', 't', 't', 'L', 't']
week = [day_1, day_2, day_3, day_4, day_5]
ttCSE3B = []
trL = {}
trT = {}
timetable3CB = []
for _ in SEC3B:
    if _ not in teachers:
        teachers[_] = [['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f']
                       ]
for _ in SEC3B:
    y = []
    for i in range(int(SEC3B[_][1][0])):
        y.append(SEC3B[_][0] + 'L')
    trL[_] = y

for _ in SEC3B:
    y = []
    for i in range(int(SEC3B[_][1][2])):
        y.append(SEC3B[_][0] + 'tut')
    trT[_] = y
"""
for _ in SEC3B:
    for i in range(int(SEC3B[_][1][4])):
        l.append(SEC3B[_][0] + 'l')
"""
for i in range(0, 5):
    x = random.randint(0, len(week) - 1)
    y = week.pop(x)
    timetable3CB.append(y)

for i in range(0, 5):
    while timetable3CB[i][0] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][0] == 'f':
            timetable3CB[i][0] = trL[x].pop(0)
            teachers[x][i][0] = 'SEM3SECB'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while timetable3CB[i][2] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][2] == 'f':
            timetable3CB[i][2] = trL[x].pop(0)
            teachers[x][i][2] = 'SEM3SECB'
        elif len(trL[x]) == 0:
            y = trL.pop(x)
if len(trL) != 0:
    for i in range(0, 5):
        while timetable3CB[i][3] == 'L' and len(trL) != 0:
            x = random.choice(list(trL))
            if len(trL[x]) != 0 and teachers[x][i][3] == 'f':
                timetable3CB[i][3] = trL[x].pop(0)
                teachers[x][i][3] = 'SEM3SECB'
            elif len(trL[x]) == 0:
                y = trL.pop(x)
            if len(trL) == 0:
                break
        if len(trL) == 0:
            break

for i in range(0, 5):
    while timetable3CB[i][1] == 'l' and len(labB) != 0:
        x = random.randint(0, len(labB) - 1)
        if labB[x] != ttCSE3A[i][1]:
            timetable3CB[i][1] = labB.pop(x)
        if len(labB) == 0:
            break
    if len(labB) == 0:
        break


for i in range(0, 5):
    while timetable3CB[i][1] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][1] == 'f':
            timetable3CB[i][1] = trT[x].pop(0)
            teachers[x][i][1] = 'SEM3SECB'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0:
            break
    if len(trT) == 0:
        break

for i in range(0, 5):
    while timetable3CB[i][2] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][2] == 'f':
            timetable3CB[i][2] = trT[x].pop(0)
            teachers[x][i][2] = 'SEM3SECB'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0:
            break
    if len(trT) == 0:
        break

for i in range(0, 5):
    while timetable3CB[i][3] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][3] == 'f':
            timetable3CB[i][3] = trT[x].pop(0)
            teachers[x][i][3] = 'SEM3SECB'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0:
            break
    if len(trT) == 0:
        break

for i in range(0, 5):
    if len(timetable3CB[i]) > 4:
        while timetable3CB[i][4] == 't' and len(trT) != 0:
            x = random.choice(list(trT))
            if len(trT[x]) != 0 and (len(teachers[x][i]) == 4 or teachers[x][i][3] == 'f'):
                timetable3CB[i][4] = trT[x].pop(0)
                teachers[x][i].append('SEM3SECB')
            elif len(trT[x]) == 0:
                y = trT.pop(x)
            break
    if len(trT) == 0:
        break

ttCSE3B = timetable3CB
# for i in range(len(ttCSE3B)):
#     print(ttCSE3B[i])

