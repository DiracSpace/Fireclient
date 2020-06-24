#!/usr/bin/env python
from modules import deleteFunctions, addFunctions
from google.cloud import firestore
import json

#json = json.loads(open('links.json').read())

version = '0.1.5'

logo = f"""
 /$$$$$$$$ /$$                               /$$ /$$                       /$$
| $$_____/|__/                              | $$|__/                      | $$
| $$       /$$  /$$$$$$   /$$$$$$   /$$$$$$$| $$ /$$  /$$$$$$  /$$$$$$$  /$$$$$$
| $$$$$   | $$ /$$__  $$ /$$__  $$ /$$_____/| $$| $$ /$$__  $$| $$__  $$|_  $$_/
| $$__/   | $$| $$  \__/| $$$$$$$$| $$      | $$| $$| $$$$$$$$| $$  \ $$  | $$
| $$      | $$| $$      | $$_____/| $$      | $$| $$| $$_____/| $$  | $$  | $$ /$$
| $$      | $$| $$      |  $$$$$$$|  $$$$$$$| $$| $$|  $$$$$$$| $$  | $$  |  $$$$/
|__/      |__/|__/       \_______/ \_______/|__/|__/ \_______/|__/  |__/   \___/
                                                                by DiracSpace
                                                                Version {version}
"""

firestoreJsonError = "'export GOOGLE_APPLICATION_CREDENTIALS='/path/to/keyfile.json'"
docuids = []
options = ["Delete field from all docs in collection", "Delete field from one doc in a collection", "Delete all docs from collection",
"Delete doc from collection", "Read all docs from collection", "Read all docs and data from collection","Add field to all docs in collection",
"Add field/value from another collection to a document in collection", "Add same field but different value to all docs in collection",
"Add new document with N fields", "Add all documents from one collection to another", "Add document N times with different values", "Add data from JSON file",
"Read all docs from collection using filters"]

good = '\033[92m[+]\033[0m'

try:
    db = firestore.Client()
except Exception as e:
    print (f'Google credentials not detected, run {firestoreJsonError}')
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
    print ('\n')
    return docuids

def readAllDocsFromCollectionWithFilter(db, collection):
    field = input('Field name -> ')
    value = input(f'Where {field} == what? -> ')
    print (f"Reading document uid's from {collection}")
    print ('\n')
    ref_obj = db.collection(collection).where(field, "==", value)
    for doc in ref_obj.stream():
        id = doc.id
        values = doc.to_dict()
        print (f'%s{doc.id}' % good)

def readAllDocsAndDataFromCollection(db, collection):
    dataset = []
    print (f"Reading document uid's from {collection}")
    print ('\n')
    ref_obj = db.collection(collection)
    for doc in ref_obj.stream():
        id = doc.id
        values = doc.to_dict()
        dataset.append(values)
        print (f'%s{doc.id}' % good)
        print (*values.items(), sep='\n')
        print ('\n')
    answer = input('Do you want to create JSON file? (Y/n) -> ')
    if answer == 'Y':
        dumpToJSONFile(collection, dataset)
    print ('Finished')

def addCopiedValueFromAnotherDocToDocInAnotherCollection(db):
    collection = input('Collection name -> ')
    field = input('Field name -> ')

def geturl(key):
    try:
        value = json[f'{key}']
        return value
    except Exception as e:
        print (f'Error getting url -> {e}')

def readJSONFile(file):
    input = open(file)
    json_array = json.load(input)
    dataset = []
    for index, item in enumerate(json_array):
        dataset.append(item)
    return dataset

def dumpToJSONFile(collection, dataset):
    with open(f'{collection}.json', 'w') as outfile:
        json.dump(dataset, outfile)
    print (f'Created JSON file {collection}.json in current working directory')
    print ('\n')

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
        for index, uid in enumerate(docsObtained):
            print (f'{index} => {uid}')
        print ('\n')
        answer = input('All - one field or one - one field? (a/b) -> ')
        if answer == 'a':
            addFunctions.adduidArrayToField(db, docsObtained)
        else:
            addFunctions.addSameFieldDifferentValueToAllDocsInCollection(db, docsObtained)
    elif option == 5:
        collection = input('Collection name -> ')
        readAllDocsAndDataFromCollection(db, collection)
    elif option == 6:
        addFunctions.addFieldToAllDocsInCollection(db)
    elif option == 7:
        print ('not yet bruh')
    elif option == 8:
        data = []
        addFunctions.addSameFieldDifferentValueToAllDocsInCollection(db, data)
    elif option == 9:
        collection = input('To which collection should I add your doc? -> ')
        quantity = int(input('How much fields? -> '))
        addFunctions.addDocumentsToCollection(db, quantity, collection)
        print ('Finished')
    elif option == 10:
        addFunctions.addAllDocsFromCollectionToCollection(db)
    elif option == 11:
        addFunctions.addDocNTimesWithDifferentValues(db)
    elif option == 12:
        addFunctions.addDataFromJSONFile(db)
    elif option == 13:
        collection = input('Collection name -> ')
        readAllDocsFromCollectionWithFilter(db, collection)

if __name__ == '__main__':
    print (logo)
    while True:
        try:
            mainProcess(db)
        except KeyboardInterrupt:
            print("\n\n\tBye!")
            exit()
