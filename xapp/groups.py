from bson.objectid import ObjectId
from xapp.models import GROUPS_COLLECTION
from flask_login import current_user
import datetime


class AddGroup(object):
    def __init__(self, name, users=None, timestamp=None, simplify=False):
        self.name = name
        self.timestamp = datetime.datetime.utcnow()
        self.users = users
        self.users.append(current_user.get_id())
        self.simplify = simplify

    def addGroup():
        GROUP_ID = GROUPS_COLLECTION.insert_one({
                        'name': self.name, 'timestamp': self.timestamp, 'members': self.users
                        }).inserted_id
        return GROUP_ID


class Group(object):
    def __init__(self, groupID):
        self.groupID = groupID

    def addUsers(self, users):
        GROUP_COLLECTION.find_one_and_update({'_id': ObjectId(self.groupID)}, {'$addToSet': {'users': users}})

    def addBill(self, billID):
        GROUP_COLLECTION.find_one_and_update({'_id': ObjectId(self.groupID)}, {'addToSet': {'bills': billID}})

    def addSimplify(self, simplify)
        GROUP_COLLECTION.find_one_and_update({'_id': ObjectId(self.groupID)}, {'addToSet': {'simplify': simplify}})
