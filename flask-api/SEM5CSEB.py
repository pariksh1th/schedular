from user_input import SEC5B
from SEM5CSE import tt5CSB
from SEM5CSEA import teachers, l2, tt5CSA
import random

trL = {}
trT = {}
for _ in SEC5B:
    if _ not in teachers:
        teachers[_] = [['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f']
                       ]
for _ in SEC5B:
    y = []
    for i in range(int(SEC5B[_][1][0])):
        y.append(SEC5B[_][0] + 'L')
    trL[_] = y
for _ in SEC5B:
    y = []
    for i in range(int(SEC5B[_][1][2])):
        y.append(SEC5B[_][0] + 'tut')
    trT[_] = y

t = 0
for i in range(0, 5):
    while tt5CSB[i][2] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        t += 1
        if len(trL[x]) != 0 and teachers[x][i][2] == 'f':
            tt5CSB[i][2] = trL[x].pop(0)
            teachers[x][i][2] = 'SEM5SECB'
        elif len(trL[x]) == 0:
            y = trL.pop(x)
        if len(trL) == 0 or t > 30:
            break
    if len(trL) == 0 or t > 30:
        break

t = 0
for i in range(0, 5):
    while tt5CSB[i][1] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        t += 1
        if len(trL[x]) != 0 and teachers[x][i][1] == 'f':
            tt5CSB[i][1] = trL[x].pop(0)
            teachers[x][i][1] = 'SEM5SECB'
        elif len(trL[x]) == 0:
            y = trL.pop(x)
        if len(trL) == 0 or t > 30:
            break
    if len(trL) == 0 or t > 30:
        break

for i in range(0, 5):
    while tt5CSB[i][0] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][0] == 'f':
            tt5CSB[i][0] = trL[x].pop(0)
            teachers[x][i][0] = 'SEM5SECB'
        elif len(trL[x]) == 0:
            y = trL.pop(x)
        if len(trL) == 0:
            break
    if len(trL) == 0:
        break

for i in range(0, 5):
    while tt5CSB[i][3] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][3] == 'f':
            tt5CSB[i][3] = trL[x].pop(0)
            teachers[x][i][3] = 'SEM5SECB'
        elif len(trL[x]) == 0:
            y = trL.pop(x)
        if len(trL) == 0:
            break
    if len(trL) == 0:
        break

for i in range(0, 5):
    while tt5CSB[i][0] == 'l' and len(l2) != 0:
        x = random.randint(0, len(l2) - 1)
        if l2[x] != tt5CSA[i][0]:
            tt5CSB[i][0] = l2.pop(x)
        if len(l2) == 0:
            break
    if len(l2) == 0:
        break
t = 0

for i in range(0, 5):
    while tt5CSB[i][3] == 't' and len(trT) != 0:
        t += 1
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][3] == 'f':
            tt5CSB[i][3] = trT[x].pop(0)
            teachers[x][i][3] = 'SEM5SECB'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0 or t > 31:
            break
    if len(trT) == 0 or t > 31:
        break

for i in range(0, 5):
    while tt5CSB[i][0] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][0] == 'f':
            tt5CSB[i][0] = trT[x].pop(0)
            teachers[x][i][0] = 'SEM5SECB'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0:
            break
    if len(trT) == 0:
        break

for _ in teachers:
    for i in range(5):
        if len(teachers[_][i]) == 4 and teachers[_][i][1] != 'f':
            teachers[_][i].insert(2, teachers[_][i][1])
        elif len(teachers[_][i]) == 4:
            teachers[_][i].insert(2, 'f')