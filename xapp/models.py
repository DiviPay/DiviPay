import os
from pymongo import MongoClient

DATABASE_URI = 'xapp'

DATABASE = MongoClient(DATABASE_URI)
db = DATABASE.get_default.database()


