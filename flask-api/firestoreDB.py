

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

def testing(userId):
    res = db.collection('courses').where('userID', '==', userId).get()

    if res:
        for doc in res:
            return doc.to_dict()
    
def test():
    return testing('46N64qo1bxe7VrcXadiztikzFDs2')


sec_names = ['Section 1', 'Section 2', 'Section 3', 'Section 4', 'Section 5', 'Section 6']


def sec_test(userId, secs):
    print('workings')
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

    
    
test_user = '46N64qo1bxe7VrcXadiztikzFDs2'


def farmateOutput(data):
    output = {}
    for sec in sec_names:
        temp = {}
        for i in range(len(data[sec])):
            temp[data[sec][i]['instructor']] = [data[sec][i]['code'], f"{data[sec][i]['lecture']}-{data[sec][i]['tutorial']}-{data[sec][i]['lab']}"]
            
        output[sec] = temp
    return output
        