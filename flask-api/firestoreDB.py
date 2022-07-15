

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


