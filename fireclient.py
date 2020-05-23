#!/usr/bin/env python
import subprocess, deleteFunctions, addFunctions
from google.cloud import firestore

logo = """
 /$$$$$$$$ /$$                               /$$ /$$                       /$$
| $$_____/|__/                              | $$|__/                      | $$
| $$       /$$  /$$$$$$   /$$$$$$   /$$$$$$$| $$ /$$  /$$$$$$  /$$$$$$$  /$$$$$$
| $$$$$   | $$ /$$__  $$ /$$__  $$ /$$_____/| $$| $$ /$$__  $$| $$__  $$|_  $$_/
| $$__/   | $$| $$  \__/| $$$$$$$$| $$      | $$| $$| $$$$$$$$| $$  \ $$  | $$
| $$      | $$| $$      | $$_____/| $$      | $$| $$| $$_____/| $$  | $$  | $$ /$$
| $$      | $$| $$      |  $$$$$$$|  $$$$$$$| $$| $$|  $$$$$$$| $$  | $$  |  $$$$/
|__/      |__/|__/       \_______/ \_______/|__/|__/ \_______/|__/  |__/   \___/
                                                                by DiracSpace
"""

firestoreJsonError = "'export GOOGLE_APPLICATION_CREDENTIALS='/path/to/keyfile.json'"
docuids = []
options = ["Delete field from all docs in collection", "Delete field from one doc in a collection", "Delete all docs from collection",
"Delete doc from collection", "Read all docs from collection", "Read all docs and data from collection","Add field to all docs in collection", "Add field/value from another collection to a document in collection"]

good = '\033[92m[+]\033[0m'

try:
    db = firestore.Client()
except Exception as e:
    print (f'GOOGLE_APPLICATION_CREDENTIALS error appeared, run {firestoreJsonError}')
    exit()

def printOptions():
    for index, option in enumerate(options):
        good = f'\033[92m{index}\033[0m'
        square = f'\033[91m[{good}]\033[0m'
        print (f'%s {option}' % square)
    print ('\n')

def readAllDocsFromCollection(db, collection):
    print (f"Reading document uid's from {collection}")
    print ('\n')
    ref_obj = db.collection(collection)
    for doc in ref_obj.stream():
        docuids.append(doc.id)
    return docuids

def readAllDocsAndDataFromCollection(db, collection):
    print (f"Reading document uid's from {collection}")
    print ('\n')
    ref_obj = db.collection(collection)
    for doc in ref_obj.stream():
        values = doc.to_dict()
        print (f'%s{doc.id}' % good)
        print (*values.items(), sep='\n')
        print ('\n')

def addCopiedValueFromAnotherDocToDocInAnotherCollection(db):
    collection = input('Collection name -> ')
    field = input('Field name -> ')

def mainProcess(db):
    print ('\n')
    printOptions()
    option = int(input('What ya wanna do? '))
    print ('\n')
    if option == 0:
        deleteFunctions.deleteFieldFromAllDocsInCollection(db)
    elif option == 1:
        deleteFunctions.deleteFieldFromDoc(db)
    elif option == 2:
        deleteFunctions.deleteAllDocsFromCollection(db)
    elif option == 3:
        deleteFunctions.deleteDocFromCollection(db)
    elif option == 4:
        collection = input('Collection name -> ')
        docsObtained = readAllDocsFromCollection(db, collection)
        for index, doc in enumerate(docsObtained):
            print (f'[{index}] => {doc}')
    elif option == 5:
        collection = input('Collection name -> ')
        readAllDocsAndDataFromCollection(db, collection)
    elif option == 6:
        addFunctions.addFieldToAllDocsInCollection(db)

if __name__ == '__main__':
    print (logo)
    while True:
        try:
            mainProcess(db)
        except KeyboardInterrupt:
            print("\n\n\tBye!")
            exit()
