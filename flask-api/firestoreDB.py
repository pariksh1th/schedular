

import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def queryWith(userId, sectionName):
    
    res = db.collection('courses').where('userID', '==', userId).where('sectionName', '==', sectionName).get()
    output = []
    if res:
        for doc in res:
            output.append(doc.to_dict())
    
    return output

# def testing(userId):
#     res = db.collection('courses').where('userID', '==', userId).get()

#     if res:
#         for doc in res:
#             return doc.to_dict()
    
# def test():
#     return testing('46N64qo1bxe7VrcXadiztikzFDs2')


SECTIONS = [
"SEM 3 Section A" ,
"SEM 3 Section B" ,
"SEM 5 Theory Basket Electives" ,
"SEM 5 Electives" ,
"SEM 5 Section A",
"SEM 5 Section B",
"SEM 3 ECE",
"SEM 3 DSA",
"SEM 5 ECE",
"SEM 5 DSA",
# "SEM 7",
"SEM 7 ECE",

]

"""  SECTIONS = [
"SEM 3 Section A" ,
"SEM 3 Section B" ,
"SEM 5 Theory Basket Electives" ,
"SEM 5 Electives" ,
"SEM 5 Section A",
"SEM 5 Section B",
"SEM 3 ECE",
"SEM 3 DSA",
"SEM 5 ECE",
"SEM 5 DSA",
# "SEM 7",
"SEM 7 ECE",
]  """



def sec_test(secs):
    from main import test_user
    userId = test_user
    print('workings')
    print('userid',userId)
    outputDict = {}
    for i in secs:
        doc_list = []
        res = db.collection('courses').where('userID', '==', userId).where('sectionName', '==', i).get()
        if res:
            for doc in res:
                doc_list.append(doc.to_dict())
        outputDict[i] = doc_list

    # return outputDict
    return farmateOutput(outputDict)

    
    
# test_user = '46N64qo1bxe7VrcXadiztikzFDs2'


def farmateOutput(data):
    output = {}
    for sec in SECTIONS:
        temp = {}
        for i in range(len(data[sec])):
            temp[data[sec][i]['instructor']] = [data[sec][i]['code'], f"{data[sec][i]['lecture']}-{data[sec][i]['tutorial']}-{data[sec][i]['lab']}"]
            
        output[sec] = temp
    return output
        