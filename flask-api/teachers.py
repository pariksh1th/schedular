from user_input import *
from SEM3CSEA import ttCSE3A

teachers = {}

for _ in SEC3A:
    flag = 0
    for i in teachers:
        if i == _:
            flag = 1
    if flag == 0:
        teachers[_] = [['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f'],
                       ['f', 'f', 'f', 'f']
                       ]

for _ in teachers:
    for i in range(0, 5):
        if ttCSE3A[i][0] == (SEC3A[_][0] + 'L'):
            teachers[_][i][0] = 'SEM3CSEA'
        if ttCSE3A[i][2] == (SEC3A[_][0] + 'L'):
            teachers[_][i][2] = 'SEM3CSEA'
        elif ttCSE3A[i][3] == (SEC3A[_][0] + 'L') and len(ttCSE3A[i]) == 5:
            teachers[_][i][1] = 'f'
            teachers[_][i][2] = 'f'
            teachers[_][i][3] = 'SEM3CSEA'
            teachers[_][i].append('f')
        if ttCSE3A[i][3] == (SEC3A[_][0] + 'L') and len(ttCSE3A[i]) == 4:
            teachers[_][i][3] = 'SEM3CSEA'
        if ttCSE3A[i][1] == (SEC3A[_][0] + 'tut'):
            teachers[_][i][1] = 'SEM3CSEA'
        if ttCSE3A[i][2] == (SEC3A[_][0] + 'tut'):
            teachers[_][i][2] = 'SEM3CSEA'
        elif ttCSE3A[i][3] == (SEC3A[_][0] + 'tut'):
            teachers[_][i][3] = 'SEM3CSEA'
        if len(ttCSE3A[i]) == 5:
            if ttCSE3A[i][4] == (SEC3A[_][0] + 'tut'):
                teachers[_][i][4] = 'SEM3CSEA'
    if len(SEC3A[_]) > 2:
        for i in range(0, 5):
            if ttCSE3A[i][0] == (SEC3A[_][2] + 'L'):
                teachers[_][i][0] = 'SEM3CSEA'
            if ttCSE3A[i][2] == (SEC3A[_][2] + 'L'):
                teachers[_][i][2] = 'SEM3CSEA'
            elif ttCSE3A[i][3] == (SEC3A[_][2] + 'L') and len(ttCSE3A[i]) == 5:
                teachers[_][i][1] = 'f'
                teachers[_][i][2] = 'f'
                teachers[_][i][3] = 'SEM3CSEA'
                teachers[_][i].append('f')
            if len(ttCSE3A[i]) == 4 and ttCSE3A[i][3] == (SEC3A[_][2] + 'L'):
                teachers[_][i][3] = 'SEM3CSEA'

            if ttCSE3A[i][1] == (SEC3A[_][2] + 'tut'):
                teachers[_][i][1] = 'SEM3CSEA'
            if ttCSE3A[i][2] == (SEC3A[_][2] + 'tut'):
                teachers[_][i][2] = 'SEM3CSEA'
            elif ttCSE3A[i][3] == (SEC3A[_][2] + 'tut'):
                teachers[_][i][3] = 'SEM3CSEA'
            if len(ttCSE3A[i]) == 5:
                if ttCSE3A[i][4] == (SEC3A[_][2] + 'tut'):
                    teachers[_][i][4] = 'SEM3CSEA'

