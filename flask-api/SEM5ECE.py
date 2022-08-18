from user_input import SEM5ECE
from SEM3ECE import teachers
from SEM5CSE import tt5CSA
import random

day_1 = ['l', 'L', 'L', 't']
day_2 = ['l', 'L', 'L', 't']
day_3 = ['t', 'L', 'L', 'L']
day_4 = ['L', 'L', 'L', 't']
day_5 = ['t', 'L', 'L', 't']
week = [day_1, day_2, day_3, day_4, day_5]
tt5ECE = []
trL = {}
trT = {}
lab = []
l = []

for _ in SEM5ECE:
    if _ not in teachers:
        teachers[_] = [['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f']
                       ]

for _ in SEM5ECE:
    y = []
    for i in range(int(SEM5ECE[_][1][0])):
        y.append(SEM5ECE[_][0] + 'L')
    if len(SEM5ECE[_]) > 2:
        for i in range(int(SEM5ECE[_][3][0])):
            y.append(SEM5ECE[_][2] + 'L')
    trL[_] = y

for _ in SEM5ECE:
    y = []
    for i in range(int(SEM5ECE[_][1][2])):
        y.append(SEM5ECE[_][0] + 'tut')
    if len(SEM5ECE[_]) > 2:
        for i in range(int(SEM5ECE[_][3][2])):
            y.append(SEM5ECE[_][2] + 'tut')
    trT[_] = y

for _ in SEM5ECE:
    for i in range(int(SEM5ECE[_][1][4])):
        l.append(SEM5ECE[_][0] + 'p')
    if len(SEM5ECE[_]) > 2:
        for i in range(int(SEM5ECE[_][1][4])):
            l.append(SEM5ECE[_][2] + 'p')


if len(l) == 1:
    l = [l[0], l[0]]
elif len(l) == 2:
    l = [l[0], l[0], l[1], l[1]]
elif len(l) == 3:
    l = [l[0] + '/' + l[1], l[0] + '/' + l[1], l[2], l[2]]
elif len(l) == 4:
    l = [l[0] + '/' + l[1], l[0] + '/' + l[1], l[2] + '/' + l[3], l[2] + '/' + l[3]]


for i in range(0, 5):
    x = random.randint(0, len(week) - 1)
    y = week.pop(x)
    tt5ECE.append(y)

for _ in range(4):
    for i in range(4):
        if tt5CSA[_][i] == 'ElectiveL':
            tt5ECE[_][i] = 'ElectiveL'
        elif tt5CSA[_][i] == 'ElectiveTut':
            tt5ECE[_][i] = 'ElectiveTut'
        elif tt5CSA[_][i] == 'Electivel':
            tt5ECE[_][1] = 'Electivel'

for i in range(0, 5):
    while tt5ECE[i][2] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][3] == 'f':
            tt5ECE[i][2] = trL[x].pop(0)
            teachers[x][i][3] = 'SEM5ECE'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while tt5ECE[i][1] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][1] == 'f' and teachers[x][i][2] == 'f':
            tt5ECE[i][1] = trL[x].pop(0)
            teachers[x][i][1] = teachers[x][i][2] = 'SEM5ECE'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while tt5ECE[i][0] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][0] == 'f':
            tt5ECE[i][0] = trL[x].pop(0)
            teachers[x][i][0] = 'SEM5ECE'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while tt5ECE[i][3] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][4] == 'f':
            tt5ECE[i][3] = trL[x].pop(0)
            teachers[x][i][4] = 'SEM5ECE'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while tt5ECE[i][0] == 'l' and len(l) != 0:
        x = random.randint(0, len(l) - 1)
        tt5ECE[i][0] = l.pop(x)
        if len(l) == 0:
            break
    if len(l) == 0:
        break

for i in range(0, 5):
    while tt5ECE[i][0] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][0] == 'f':
            tt5ECE[i][0] = trT[x].pop(0)
            teachers[x][i][0] = 'SEM5ECE'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0:
            break
    if len(trT) == 0:
        break

for i in range(0, 5):
    while tt5ECE[i][3] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][4] == 'f':
            tt5ECE[i][3] = trT[x].pop(0)
            teachers[x][i][4] = 'SEM5ECE'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0:
            break
    if len(trT) == 0:
        break


