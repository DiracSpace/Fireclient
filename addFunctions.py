#!/usr/bin/env python
import fireclient

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
