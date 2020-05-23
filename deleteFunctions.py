#!/usr/bin/env python
import fireclient

def deleteFieldFromAllDocsInCollection(db):
    collection = input('Collection name -> ')
    field = input('Field name -> ')
    documents = readAllDocsFromCollection(db, collection)
    for index, uid in enumerate(documents):
        print (f'{index} => deleting {field} from {collection} in {documents[index]}')
        delete_ref = db.collection(collection).document(documents[index])
        delete_ref.update({
            field : firestore.DELETE_FIELD
        })
    print ('Finished \n')

def deleteAllDocsFromCollection(db):
    collection = input('Collection name -> ')
    documents = fireclient.readAllDocsFromCollection(db, collection)
    for index, uid in enumerate(documents):
        print (f'{index} => deleting {documents[index]} from {collection}')
        db.collection(collection).document(documents[index]).delete()
    print ('Finished')

def deleteFieldFromDoc(db):
    collection = input('Collection name -> ')
    document = input('Document uid -> ')
    field = input('Field name -> ')
    delete_ref = db.collection(collection).document(document)
    delete_ref.update({
        field : firestore.DELETE_FIELD
    })
    print (f'Deleted {field} from {document} in {collection}')

def deleteDocFromCollection(db):
    collection = input('Collection name -> ')
    document = input('Document uid -> ')
    db.collection(collection).document(document).delete()
    print (f'Deleted {document} from {collection}')
