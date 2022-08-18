from user_input import SEC3B
from teachers import teachers
from SEM3CSEA import ttCSE3A, labB, labcode, labs
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
labb = labB
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
    if len(SEC3B[_]) > 2:
        for i in range(int(SEC3B[_][3][0])):
            y.append(SEC3B[_][2] + 'L')
    trL[_] = y

for _ in SEC3B:
    y = []
    for i in range(int(SEC3B[_][1][2])):
        y.append(SEC3B[_][0] + 'tut')
    if len(SEC3B[_]) > 2:
        for i in range(int(SEC3B[_][3][2])):
            y.append(SEC3B[_][2] + 'tut')
    trT[_] = y
"""
for _ in SEC3B:
    for i in range(int(SEC3B[_][1][4])):
        l.append(SEC3B[_][0] + 'l')
"""

for i in range(5):
    if labcode[i] == 1:
        for j in range(len(week)):
            if len(week[j]) == 5:
                timetable3CB.append(week.pop(j))


for _ in range(len(week)):
    timetable3CB.append(week.pop(0))
        

for i in range(0, 5):
    while timetable3CB[i][0] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][0] == 'f':
            timetable3CB[i][0] = trL[x].pop(0)
            teachers[x][i][0] = 'SEM3SECB'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

t = 0
for i in range(0, 5):
    while timetable3CB[i][2] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        t += 1
        if len(trL[x]) != 0 and teachers[x][i][2] == 'f':
            timetable3CB[i][2] = trL[x].pop(0)
            teachers[x][i][2] = 'SEM3SECB'
        elif len(trL[x]) == 0:
            y = trL.pop(x)
            if len(trL) == 0 or t > 30:
                break
        if len(trL) == 0 or t > 30:
            break

t = 0
if len(trL) != 0:
    for i in range(0, 5):
        while timetable3CB[i][3] == 'L' and len(trL) != 0:
            x = random.choice(list(trL))
            t += 1
            if len(trL[x]) != 0 and teachers[x][i][3] == 'f':
                timetable3CB[i][3] = trL[x].pop(0)
                teachers[x][i][3] = 'SEM3SECB'
            elif len(trL[x]) == 0:
                y = trL.pop(x)
            if len(trL) == 0 or t > 31:
                break
        if len(trL) == 0 or t > 31:
            break


def lab(lab):
    t = 0
    for i in range(0, 5):
        while timetable3CB[i][1] == 'l' and len(lab) != 0:
            x = random.randint(0, len(lab) - 1)
            t += 1
            if lab[x] != ttCSE3A[i][1]:
                timetable3CB[i][1] = lab.pop(x)
            if len(lab) == 0 or t > 50:
                break
        if len(lab) == 0 or t > 50:
            break

lab(labB)

for i in range(0, 5):
    while timetable3CB[i][1] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][1] == 'f':
            timetable3CB[i][1] = trT[x].pop(0)
            teachers[x][i][1] = 'SEM3SECB'
            print('a')
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0:
            break
    if len(trT) == 0:
        break

t = 0
for i in range(0, 5):
    while timetable3CB[i][2] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        t += 1
        if len(trT[x]) != 0 and teachers[x][i][2] == 'f':
            timetable3CB[i][2] = trT[x].pop(0)
            teachers[x][i][2] = 'SEM3SECB'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0 or t > 30:
            break
    if len(trT) == 0 or t > 30:
        break

t = 0
for i in range(0, 5):
    while timetable3CB[i][3] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        t += 1
        if len(trT[x]) != 0 and teachers[x][i][3] == 'f':
            timetable3CB[i][3] = trT[x].pop(0)
            teachers[x][i][3] = 'SEM3SECB'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0 or t > 30:
            break
    if len(trT) == 0 or t > 30:
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

