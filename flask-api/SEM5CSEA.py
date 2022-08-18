from user_input import SEC5A
from SEM5CSE import tt5CSA, teachers
import random

trL = {}
trT = {}
l1 = []
l2 = []
for _ in SEC5A:
    if _ not in teachers:
        teachers[_] = [['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f']
                       ]
for _ in SEC5A:
    y = []
    for i in range(int(SEC5A[_][1][0])):
        y.append(SEC5A[_][0] + 'L')
    trL[_] = y

for _ in SEC5A:
    y = []
    for i in range(int(SEC5A[_][1][2])):
        y.append(SEC5A[_][0] + 'tut')
    trT[_] = y

for _ in SEC5A:
    for i in range(int(SEC5A[_][1][4])):
        l1.append(SEC5A[_][0] + 'p')
        l2.append(SEC5A[_][0] + 'p')

if len(l1) == 1:
    l1 = [l1[0], l1[0]]
    l2 = [l2[0], l2[0]]
elif len(l1) == 2:
    l1 = [l1[0], l1[0], l1[1], l1[1]]
    l2 = [l2[0], l2[0], l2[1], l2[1]]
elif len(l1) == 3:
    l1 = [l1[0] + '/' + l1[1], l1[0] + '/' + l1[1], l1[2], l1[2]]
    l2 = [l2[0] + '/' + l2[1], l2[0] + '/' + l2[1], l2[2], l2[2]]
elif len(l1) == 4:
    l1 = [l1[0] + '/' + l1[1], l1[0] + '/' + l1[1], l1[2] + '/' + l1[3], l1[2] + '/' + l1[3]]
    l2 = [l2[0] + '/' + l2[1], l2[0] + '/' + l2[1], l2[2] + '/' + l2[3], l2[2] + '/' + l2[3]]

for i in range(0, 5):
    while tt5CSA[i][2] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][2] == 'f':
            tt5CSA[i][2] = trL[x].pop(0)
            teachers[x][i][2] = 'SEM5SECA'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while tt5CSA[i][1] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][1] == 'f':
            tt5CSA[i][1] = trL[x].pop(0)
            teachers[x][i][1] = 'SEM5SECA'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while tt5CSA[i][0] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][0] == 'f':
            tt5CSA[i][0] = trL[x].pop(0)
            teachers[x][i][0] = 'SEM5SECA'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while tt5CSA[i][3] == 'L' and len(trL) != 0:
        x = random.choice(list(trL))
        if len(trL[x]) != 0 and teachers[x][i][3] == 'f':
            tt5CSA[i][3] = trL[x].pop(0)
            teachers[x][i][3] = 'SEM5SECA'
        elif len(trL[x]) == 0:
            y = trL.pop(x)

for i in range(0, 5):
    while tt5CSA[i][0] == 'l' and len(l1) != 0:
        x = random.randint(0, len(l1) - 1)
        tt5CSA[i][0] = l1.pop(x)
        if len(l1) == 0:
            break
    if len(l1) == 0:
        break

for i in range(0, 5):
    while tt5CSA[i][0] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][0] == 'f':
            tt5CSA[i][0] = trT[x].pop(0)
            teachers[x][i][0] = 'SEM5SECA'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0:
            break
    if len(trT) == 0:
        break

for i in range(0, 5):
    while tt5CSA[i][3] == 't' and len(trT) != 0:
        x = random.choice(list(trT))
        if len(trT[x]) != 0 and teachers[x][i][3] == 'f':
            tt5CSA[i][3] = trT[x].pop(0)
            teachers[x][i][3] = 'SEM5SECA'
        elif len(trT[x]) == 0:
            y = trT.pop(x)
        if len(trT) == 0:
            break
    if len(trT) == 0:
        break


