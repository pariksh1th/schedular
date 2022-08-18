import random
from user_input import SEC5Tb
from SEM3CSEB import teachers
from user_input import SEC5E

day_1 = ['l', 'L', 'L', 't']
day_2 = ['l', 'L', 'L', 't']
day_3 = ['t', 'L', 'L', 'L']
day_4 = ['L', 'L', 'L', 't']
day_5 = ['t', 'L', 'L', 't']

day_1_1 = ['t', 'L', 'L', 't']
day_2_1 = ['t', 'L', 'L', 't']
day_3_1 = ['l', 'L', 'L', 'L']
day_4_1 = ['L', 'L', 'L', 't']
day_5_1 = ['l', 'L', 'L', 't']

week1 = [day_1, day_2, day_3, day_4, day_5]
week2 = [day_1_1, day_2_1, day_3_1, day_4_1, day_5_1]
tt5CSA = []
tt5CSB = []
trL = {}
trT = {}
l = []

for _ in SEC5Tb:
    if _ not in teachers:
        teachers[_] = [['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f']
                       ]

lec = 2

for _ in SEC5Tb:
    y = []
    lec = int(SEC5Tb[_][1][0])
    for i in range(int(SEC5Tb[_][1][0])):
        y.append('BasketL')
    trL[_] = y

tut = 1

for _ in SEC5Tb:
    y = []
    tut = int(SEC5Tb[_][1][2])
    for i in range(int(SEC5Tb[_][1][2])):
        y.append('BasketTut')
    trT[_] = y

for _ in SEC5Tb:
    if int(SEC5Tb[_][1][4]) == 0:
        break
    for i in range(int(SEC5Tb[_][1][4])):
        l.append(SEC5Tb[_][0] + 'p')

# TODO EXCEPTION HANDLING FOR LABS

for i in range(0, 5):
    x = random.randint(0, len(week1) - 1)
    y = week1.pop(x)
    z = week2.pop(x)
    tt5CSA.append(y)
    tt5CSB.append(z)

Lcount = 0
while True:
    i = random.randint(0, 4)
    if Lcount >= lec: #Do this
        break
    while tt5CSA[i][1] == 'L':
        flag = 0
        for _ in trL:
            if teachers[_][i][1] != 'f':
                flag = 1
            if flag == 1:
                break
        if flag == 1:
            break
        if flag == 0:
            tt5CSA[i][1] = 'BasketL'
            tt5CSB[i][1] = 'BasketL'
            for _ in trL:
                teachers[_][i][1] = 'SEM5'
            Lcount += 1

Tcount = 0
while True:
    i = random.randint(0, 4)
    if Tcount >= tut: #Do this
        break
    while tt5CSA[i][3] == 't':
        flag = 0
        for _ in trT:
            if teachers[_][i][3] != 'f':
                flag = 1
            if flag == 1:
                break
        if flag == 1:
            break
        if flag == 0:
            tt5CSA[i][3] = 'BasketTut'
            tt5CSB[i][3] = 'BasketTut'
            for _ in trL:
                teachers[_][i][3] = 'SEM5'
            Tcount += 1

trL1 = {}
trT1 = {}
l1 = []

for _ in SEC5E:
    if _ not in teachers:
        teachers[_] = [['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f']
                       ]

lec = 2

for _ in SEC5E:
    y = []
    lec = int(SEC5E[_][1][0])
    for i in range(lec):
        y.append('BasketL')
    trL1[_] = y

tut = 1

for _ in SEC5E:
    y = []
    tut = int(SEC5E[_][1][2])
    for i in range(int(SEC5E[_][1][2])):
        y.append('BasketTut')
    trT1[_] = y

for _ in SEC5E:
    if int(SEC5E[_][1][4]) == 0:
        break
    for i in range(int(SEC5E[_][1][4])):
        l1.append(SEC5E[_][0] + 'l')

# TODO EXCEPTION HANDLING FOR LABS

Lcount = 0
while True:
    i = random.randint(0, 4)
    if Lcount >= lec: #Do this
        break
    while tt5CSA[i][1] == 'L':
        flag = 0
        for _ in trL1:
            if teachers[_][i][1] != 'f':
                flag = 1
            if flag == 1:
                break
        if flag == 0:
            tt5CSA[i][1] = 'ElectiveL'
            tt5CSB[i][1] = 'ElectiveL'
            for _ in trL1:
                teachers[_][i][1] = 'SEM5'
            Lcount += 1
        else:
            break

Tcount = 0
while True:
    i = random.randint(0, 4)
    if Tcount >= tut: #Do this
        break
    while tt5CSA[i][3] == 't':
        flag = 0
        for _ in trT1:
            if teachers[_][i][3] != 'f':
                flag = 1
            if flag == 1:
                break
        if flag == 1:
            break
        if flag == 0:
            tt5CSA[i][3] = 'ElectiveTut'
            tt5CSB[i][3] = 'ElectiveTut'
            for _ in trT1:
                teachers[_][i][3] = 'SEM5'
            Tcount += 1


