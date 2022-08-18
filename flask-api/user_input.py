import string
from firestoreDB import sec_test, SECTIONS


fetchedData = sec_test(SECTIONS)

SEC3A = fetchedData[SECTIONS[0]]
SEC3B = fetchedData[SECTIONS[1]]
SEC5Tb = fetchedData[SECTIONS[2]]
SEC5E = fetchedData[SECTIONS[3]]
SEC5A = fetchedData[SECTIONS[4]]
SEC5B = fetchedData[SECTIONS[5]]

SEM3ECE = fetchedData[SECTIONS[6]]
SEM3DS = fetchedData[SECTIONS[7]]
SEM5ECE = fetchedData[SECTIONS[8]]
SEM5DS = fetchedData[SECTIONS[9]]
SEM7ECE = fetchedData[SECTIONS[10]]


Common = ['ELE2', 'ELE6', 'ELE7', 'ELE8']
SEM7 = {
        'Malay': ['ELE1', '2-0-0'],
         'Gokulraj': ['ELE2', '2-1-0', 'ELE6', '2-1-0'],
         'Vivekraj': ['ELE3', '2-0-1'],
         'Animesh': ['ELE4', '2-1-0'],
         'Radhika': ['CS202', '2-1-1'],
         'Pramod yal': ['ELE5', '2-1-0'],
        'Tanay': ['ELE7', '2-1-0'],
        'Deepak': ['ELE8', '2-1-0']
}

print(fetchedData)

# {'Section 1': {'Promod': ['CS201', '2-0-0'], 'Vivekraj': ['CS207', '2-1-1'], 'Promod yal': ['EC105', '2-0-1'], 'Lakshman': ['MA201', '2-1-0'], 'Malay': ['CS202', '2-1-1'], 'Unkn': ['HS206', '2-0-0']}, 'Section 2': {'Unkn': ['HS206', '2-0-0'], 'Lakshman': ['MA201', '2-1-0'], 'Vivekraj': ['EC105', '2-0-1'], 'Pawan': ['CS201', '2-0-0'], 'Radhika': ['CS202', '2-1-1']}, 'Section 3': {'Pawan': ['Gra', '2-1-0'], 'Radhika': ['SEC ENG', '2-1-0']}, 'Section 4': {'Ramesh': ['CS309', '2-1-0'], 'Sadhvi': ['CS303', '2-1-1'], 'Jayalakshmi': ['CS304', '2-1-0']}, 'Section 5': {'Uma': ['Clou', '2-1-0'], 'Vivekraj': ['Com gra', '2-1-0'], 'Sadhvi': ['Com desi', '2-1-0']}, 'Section 6': {'Ramesh': ['CS309', '2-1-0'], 'Jayalakshmi': ['CS304', '2-1-0'], 'Sadhvi': ['CS303', '2-1-1']}}



# SEC3A = {'Promod': ['CS201', '2-0-0'], 'Vivekraj': ['CS207', '2-1-1'], 'Promod yal': ['EC105', '2-0-1'], 'Lakshman': ['MA201', '2-1-0'], 'Malay': ['CS202', '2-1-1'], 'Unkn': ['HS206', '2-0-0']}
# SEC3B = {'Unkn': ['HS206', '2-0-0'], 'Lakshman': ['MA201', '2-1-0'], 'Vivekraj': ['EC105', '2-0-1'], 'Pawan': ['CS201', '2-0-0'], 'Radhika': ['CS202', '2-1-1']}
# SEC5A = {'Ramesh': ['CS309', '2-1-0'], 'Sadhvi': ['CS303', '2-1-1'], 'Jayalakshmi': ['CS304', '2-1-0']}
# SEC5Tb = {'Pawan': ['Gra', '2-1-0'], 'Radhika': ['SEC ENG', '2-1-0'], 'Jayalakshmi': ['Something', '2-1-0']}
# SEC5B = {'Ramesh': ['CS309', '2-1-0'], 'Jayalakshmi': ['CS304', '2-1-0'], 'Sadhvi': ['CS303', '2-1-1']}
# SEC5E = {'Uma': ['Clou', '2-1-0'], 'Vivekraj': ['Com gra', '2-1-0'], 'Sadhvi': ['Com desi', '2-1-0']}

"""
print('Input all the teachers for Sem3 SECA with course code and L-t-l(Enter -1 to exit):')
while 1:
    z = []
    x = input()
    if x == '-1':
        break
    elif x in SEC3A:
        for i in range(2):
            y = input()
            SEC3A[x].append(y)
    else:
        for i in range(2):
            y = input()
            z.append(y)
        SEC3A[x] = z

#TODO Exception Handling


print('Input all the teachers for Sem3 SECB with course code(Enter -1 to exit):')
while 1:
    x = input()
    if x == '-1':
        break
    else:
        z = []
        for i in range(2):
            y = input()
            z.append(y)
        SEC3B[x] = z

print('Input all the Theory Basket electives for 5th sem:')
while 1:
    x = input()
    if x == '-1':
        break
    else:
        z = []
        for i in range(2):
            y = input()
            z.append(y)
        SEC5Tb[x] = z

print('Input all the Electives for 5th sem:')
while 1:
    x = input()
    if x == '-1':
        break
    else:
        z = []
        for i in range(2):
            y = input()
            z.append(y)
        SEC5E[x] = z

print('Input all the teachers for Sem5 SECA with course code(Enter -1 to exit):')
while 1:
    x = input()
    if x == '-1':
        break
    else:
        z = []
        for i in range(2):
            y = input()
            z.append(y)
        SEC5A[x] = z

print('Input all the teachers for Sem5 SECB with course code(Enter -1 to exit):')
while 1:
    x = input()
    if x == '-1':
        break
    else:
        z = []
        for i in range(2):
            y = input()
            z.append(y)
        SEC5B[x] = z"""
