from xapp import application
from bson.objectid import ObjectId
import datetime

class AddGroup():
    def __init__(self, name, timestamp=None, users=None):
        self.name = name
        self.timestamp = datetime.datetime.utcnow()
        self.users = users

    def addGroup():
        GROUP_ID = GROUPS_COLLECTION.insert_one({
                        'name': self.name, 'timestamp': self.timestamp, 'members': self.users
                        }).inserted_id
        return GROUP_ID


class Group():
    def addUsers(self, groupID, users):
        GROUP_COLLECTION.find_one_and_update({'_id': ObjectId(self.groupID)}, {'$addToSet': {'users': users}})

    def addBill(self, groupID, billID):
        GROUP_COLLECTION.find_one_and_update({'_id': ObjectId(self.groupID)}, {'addToSet': {'bills': billID}})

