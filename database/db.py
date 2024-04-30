from tinydb import TinyDB, Query
from tinydb.database import Document
from pprint import pprint
import json
User = Query()

db1=TinyDB('database/users.json', indent=4)
db2=TinyDB('database/products.json', indent=4)

users     = db1.table('Users')
stage     = db1.table('Stage')
index     = db1.table('Index')
products  = db2.table('Products') 

def get(table, user_id=None, product_type=None):

    # if table == "stage":
    #     return stage.get(doc_id=user_id)
    if table == "users":
        if user_id == None:
            return users.all()
        else:
            return users.get(doc_id=user_id)
    elif table == "index":
        return index.get(doc_id=user_id)
    elif table == "phone":
        tip = Query()
        if user_id != None:
            return db2.search(tip.user_id == user_id)
        else:
            return db2.search(tip.product_type == product_type)

    

def insert(table, data, user_id=None, product_type=None):

    # if table == "stage":
    #     doc = Document(
    #         value=data,
    #         doc_id=user_id
    #     )
    #     stage.insert(doc)
    
    if table == "users":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        users.insert(doc)
    
    elif table == "index":
        doc = Document(
            value=data,
            doc_id=user_id
        )
        index.insert(doc)

    elif table == "phone":
       doc_id = db2.insert(data)
       return doc_id
       
def upd(table, data, user_id=None, product=None):
    # if table == "stage":
    #     stage.update(data, doc_ids=[user_id])
    
    if table == "index":
        index.update(data, doc_ids=[user_id])
    if table == "phone":
        user_ids = int(get(table="index", user_id=user_id)["edit_doc"])
        print(user_ids)
        db2.update(data, doc_ids=[user_ids])
        print(db2)
def delete(product_id=None, user_id=None, uniq_id=None):
    if product_id is not None:
        q = Query()
        db2.remove(doc_ids=[product_id])
    elif uniq_id is not None:
        uniq_id = int(uniq_id)
        tab = db2.table("_default")
        q = Query()
        # db2.remove(q['_default'].uniq_id == f"{uniq_id}")
        tab.remove(q.uniq_id==uniq_id)
        print("O'chirildi")
    
  