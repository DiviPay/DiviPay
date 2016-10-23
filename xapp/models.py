import os
from pymongo import MongoClient

DATABASE = MongoClient('localhost', 27017)
#DATABASE.drop_database('divipay')
db = DATABASE['divipay']

GROUPS_COLLECTION = db.groups
USERS_COLLECTION = db.users
BILLS_COLLECTION = db.bills
TRANSACTION_COLLECTION = db.transactions
CURRENCY_COLLECTION = db.currencies
