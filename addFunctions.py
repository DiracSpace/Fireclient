#!/usr/bin/env python
import fireclient
from pathlib import Path

good = '\033[92m[+]\033[0m'

def addFieldToAllDocsInCollection(db):
    collection = input('Collection name -> ')
    documents = fireclient.readAllDocsFromCollection(db, collection)
    field = input('Field name -> ')
    content = input('Content -> ')
    for index, uid in enumerate(documents):
        print (f'%s{index} => adding {field} to doc {documents[index]}' % good)
        pedidos_ref = db.collection(collection).document(documents[index])
        pedidos_ref.set({
            field : content
        }, merge = True)
    print ('Finished')

def adduidArrayToField(db, array):
    collection = input('Collection name -> ')
    documents = fireclient.readAllDocsFromCollection(db, collection)
    for index, doc in enumerate(documents):
        print (f'[{index}] => {doc}')
    print ('\n')
    answer = input('Do I add same field to all docs? (y/N) -> ')
    if answer == 'n':
        field = input('Field name -> ')
        array_ref = db.collection(collection).document(doc)
        array_ref.set({
            field : array
        }, merge = True)
        print ('Finished')
    else:
        field = input('Field name -> ')
        for index, uid in enumerate(documents):
            print (f'%s{index} => adding {field} to doc {documents[index]}' % good)
            array_ref = db.collection(collection).document(documents[index])
            array_ref.set({
                field : array
            }, merge = True)
    print ('Finished')


def addSameFieldDifferentValueToAllDocsInCollection(db):
    contents = []
    collection = input('Collection name -> ')
    field = input('Field name -> ')
    documents = fireclient.readAllDocsFromCollection(db, collection)
    for index, doc in enumerate(documents):
        print (f'[{index}] => {doc}')
    print ('\n')
    answer = input('Do you want to read data from files? (y/N) ->')
    if answer == 'y':
        print ('Reading from local json file')
        for index, uid in enumerate(documents):
            jsonvalue = str(fireclient.geturl(uid))
            print (f'{index} => adding {jsonvalue} to {uid}')
            field_ref = db.collection(collection).document(documents[index])
            field_ref.set({
                field : jsonvalue
            }, merge = True)
    else:
        for index, uid in enumerate(documents):
            content = input('Content -> ')
            content_ref = db.collection(collection).document(documents[index])
            content_ref.set({
                field : content
            }, merge = True)
        print ('Finished')

def addAllDocsFromCollectionToCollection(db):
    collection = input('Collection to copy -> ')
    collectiontocopy = input('Collection to add -> ')
    print (f"Reading document uid's from {collection}")
    print ('\n')
    ref_obj = db.collection(collection)
    for doc in ref_obj.stream():
        id = doc.id
        values = doc.to_dict()
        db.collection(collection).document().set(values)
        print (f'Copying {id} from {collection} to {collectiontocopy}')
    print ('Finished')
