from models import TRANSACTION_COLLECTION
from bson.objectid import ObjectId
import datetime

class AddTransaction(object):
    def __init__(self, amount, type_of_expense='credit', description=None, tags=None):
        self.amount = amount
        self.type_of_expense = type_of_expense
        self.description = description
        self.tags = tags
        self.transaction_id = None
        self.datetime = datetime.datetime.utcnow()

    def insert_entry(self):
        self.transaction_id = TRANSACTION_COLLECTION.insert({
            'amount': self.amount,
            'date': self.datetime,
            'expense_type': self.type_of_expense,
            'description': self.description,
            'tags': self.tags
        })
        return self.transaction_id

class Transaction(object):
    def __init__(self, transaction_id):
        self.transaction_id = ObjectId(transaction_id)

    def update_amount(self, amount):
        data = {
            'amount': amount
        }
        TRANSACTION_COLLECTION.update({'_id': self.transaction_id}, {'$set': data})

    def update_expense_type(self, expense_type):
        data = {
            'expense_type': expense_type
        }
        TRANSACTION_COLLECTION.update({'_id': self.transaction_id}, {'$set': data})

    def update_description(self, description):
        data = {
            'description': description
        }
        TRANSACTION_COLLECTION.update({'_id': self.transaction_id}, {'$set': data})

    def update_tags(self, tags):
        data = {
            'tags': tags,
        }
        TRANSACTION_COLLECTION.update({'_id': self.transaction_id}, {'$set': data})
