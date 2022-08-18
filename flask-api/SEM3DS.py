from user_input import SEM3DS
from SEM7ECE import teachers
import random

day_1 = ['L', 'l', 'L', 'L']
day_2 = ['L', 'l', 'L', 'L']
day_3 = ['L', 'l', 'L', 'L']
day_4 = ['L', 'l', 'L', 't']
day_5 = ['L', 't', 't', 'L', 't']
week = [day_1, day_2, day_3, day_4, day_5]
ttDS3 = []
trL = {}
trT = {}
labA = []
l = []
for _ in SEM3DS:
    if _ not in teachers:
        teachers[_] = [['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f', 'f']
                       ]

for _ in SEM3DS:
    y = []
    for i in range(int(SEM3DS[_][1][0])):
        y.append(SEM3DS[_][0] + 'L')
    if len(SEM3DS[_]) > 2:
        for i in range(int(SEM3DS[_][3][0])):
            y.append(SEM3DS[_][2] + 'L')
    trL[_] = y

for _ in SEM3DS:
    y = []
    for i in range(int(SEM3DS[_][1][2])):
        y.append(SEM3DS[_][0] + 'tut')
    if len(SEM3DS[_]) > 2:
        for i in range(int(SEM3DS[_][3][2])):
            y.append(SEM3DS[_][2] + 'tut')
    trT[_] = y

for _ in SEM3DS:
    for i in range(int(SEM3DS[_][1][4])):
        l.append(SEM3DS[_][0] + 'p')
    if len(SEM3DS[_]) > 2:
        for i in range(int(SEM3DS[_][1][4])):
            l.append(SEM3DS[_][2] + 'p')

if len(l) == 1:
    l = [l[0], l[0]]
elif len(l) == 2:
    l = [l[0], l[0], l[1], l[1]]
elif len(l) == 3:
    l = [l[0] + '/' + l[1], l[0] + '/' + l[1], l[2], l[2]]
elif len(l) == 4:
    l = [l[0] + '/' + l[1], l[0] + '/' + l[1], l[2] + '/' + l[3], l[2] + '/' + l[3]]

labA = l
labs = len(l)

for i in range(0, 5):
    x = random.randint(0, len(week) - 1)
    y = week.pop(x)
    ttDS3.append(y)


for i in range(0, 5):
    while ttDS3[i][0] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][0] == 'f':
            ttDS3[i][0] = trL[x].pop(0)
            teachers[x][i][0] = 'SEM3DS'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

t = 0
for i in range(0, 5):
    while ttDS3[i][2] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        t += 1
        if len(trL[x]) != 0 and teachers[x][i][3] == 'f':
            ttDS3[i][2] = trL[x].pop(0)
            teachers[x][i][3] = 'SEM3DS'
        elif len(trL[x]) == 0:
            y = trL.pop(x)
            if len(trL) == 0 or t > 30:
                break
        if len(trL) == 0 or t > 30:
            break

t = 0
if len(trL) != 0:
    for i in range(0, 5):
        while ttDS3[i][3] == 'L' and len(trL) != 0:
            x = random.choice(list(trL))
            t += 1
            if len(trL[x]) != 0 and teachers[x][i][4] == 'f':
                ttDS3[i][3] = trL[x].pop(0)
                teachers[x][i][4] = 'SEM3DS'
            elif len(trL[x]) == 0:
                y = trL.pop(x)
            if len(trL) == 0 or t > 31:
                break
        if len(trL) == 0 or t > 31:
            break

lab = l
while len(lab) != 0:
    x = random.randint(0, len(ttDS3) - 1)
    if ttDS3[x][1] == 'l':
        y = random.randint(0, len(lab) - 1)
        ttDS3[x][1] = lab.pop(y)


for i in range(0, 5):
    while ttDS3[i][1] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][1] == 'f':
            ttDS3[i][1] = trT[x].pop(0)
            teachers[x][i][1] = 'SEM3DS'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0:
            break

    if len(trT) == 0:
        break

t = 0
for i in range(0, 5):
    while ttDS3[i][2] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        t += 1
        if len(trT[x]) != 0 and teachers[x][i][2] == 'f':
            ttDS3[i][2] = trT[x].pop(0)
            teachers[x][i][2] = 'SEM3DS'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0 or t > 30:
            break
    if len(trT) == 0 or t > 30:
        break
