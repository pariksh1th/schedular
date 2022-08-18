from user_input import SEM7
from SEM5CSEB import teachers
import random

day_1 = ['L', 'L', 'L', 't', 'L', 't']
day_2 = ['L', 'L', 'L', 't', 'L', 't']
day_3 = ['L', 'L', 'L', 't', 'L', 't']
day_4 = ['L', 'L', 'L', 't', 'L', 't']
day_5 = ['L', 'L', 'L', 't', 'L', 't']
trL = {}
trT = {}
timetable7 = [day_1, day_2, day_3, day_4, day_5]
for _ in SEM7:
    if _ not in teachers:
        teachers[_] = [['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f']
                       ]

for _ in SEM7:
    y = []
    for i in range(int(SEM7[_][1][0])):
        y.append(SEM7[_][0] + 'L')
    if len(SEM7[_]) > 2:
        for i in range(int(SEM7[_][3][0])):
            y.append(SEM7[_][2] + 'L')
    trL[_] = y

for _ in SEM7:
    y = []
    for i in range(int(SEM7[_][1][2])):
        y.append(SEM7[_][0] + 'tut')
    if len(SEM7[_]) > 2:
        for i in range(int(SEM7[_][3][2])):
            y.append(SEM7[_][2] + 'tut')
    trT[_] = y

l = []
for _ in SEM7:

    for i in range(int(SEM7[_][1][4])):
        l.append(SEM7[_][0] + 'p')
    if len(SEM7[_]) > 2:
        for i in range(int(SEM7[_][1][4])):
            l.append(SEM7[_][2] + 'p')

for i in range(0, 5):
    while timetable7[i][0] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][0] == 'f':
            timetable7[i][0] = trL[x].pop(0)
            teachers[x][i][0] = 'SEM7'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while timetable7[i][1] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][1] == 'f':
            timetable7[i][1] = trL[x].pop(0)
            teachers[x][i][1] = 'SEM7'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while timetable7[i][2] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][2] == 'f':
            timetable7[i][2] = trL[x].pop(0)
            teachers[x][i][2] = 'SEM7'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

t = 0
for i in range(0, 5):
    while timetable7[i][3] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        t += 1
        if len(trT[x]) != 0 and teachers[x][i][3] == 'f':
            timetable7[i][3] = trT[x].pop(0)
            teachers[x][i][3] = 'SEM7'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0 or t > 30:
            break
    if len(trT) == 0 or t > 30:
        break

t = 0
for i in range(0, 5):
    while timetable7[i][3] == 't' and len(l) != 0:
        timetable7[i][3] = l.pop()

t = 0
for i in range(0, 5):
    while timetable7[i][4] == 'L' and len(trL) != 0:
        t += 1
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][4] == 'f':
            timetable7[i][4] = trL[x].pop(0)
            teachers[x][i][4] = 'SEM7'
        elif len(trL[x]) == 0:
            y = trL.pop(x)
        if len(trL) == 0 or t > 30:
            break
    if len(trL) == 0 or t > 30:
        break
t = 0
for i in range(0, 5):
    while timetable7[i][5] == 't' and len(trT) != 0:
        t += 1
        x = random.choice(list(trT))
        if len(trT[x]) != 0:
            timetable7[i][5] = trT[x].pop(0)
            teachers[x][i].append('SEM7')
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0 or t > 30:
            break
    if len(trT) == 0 or t > 30:
        break


for i in range(0, 5):
    if timetable7[i][5] == 't' and len(l) != 0:
        timetable7[i][5] = l.pop(0)

for i in range(0, 5):
    while timetable7[i][5] == 't' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0:
            timetable7[i][5] = trL.pop(x)
            teachers[x][i].append('SEM7')
        elif len(trL[x]) == 0:
            y = trL.pop(x)
        if len(trL) == 0:
            break
    if len(trL) == 0:
        break

