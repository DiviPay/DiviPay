import os
from pymongo import MongoClient

DATABASE_URI = 'xapp'

DATABASE = MongoClient(DATABASE_URI)
db = DATABASE.get_default.database()

GROUPS_COLLECTION = db.groups
USERS_COLLECTION = db.users
BILLS_COLLECTION = db.bills
TRANSACTION_COLLECTION = db.transactions
