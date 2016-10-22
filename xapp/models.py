import os
from pymongo import MongoClient

DATABASE = MongoClient('localhost', 27017)
db = DATABASE['xapp']

GROUPS_COLLECTION = db.groups
USERS_COLLECTION = db.users
BILLS_COLLECTION = db.bills
TRANSACTION_COLLECTION = db.transactions

TRANSACTION_COLLECTION.drop()
