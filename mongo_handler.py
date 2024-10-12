import pymongo

class MongoHandler:
    def __init__(self, uri, db_name):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db['pdf_documents']

    def insert_document(self, document):
        self.collection.insert_one(document)

    def update_document(self, document_name, summary, keywords):
        self.collection.update_one(
            {'document_name': document_name},
            {'$set': {'summary': summary, 'keywords': keywords}}
        )
