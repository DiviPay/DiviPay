from xapp.models import USERS_COLLECTION
from flask_login import UserMixin
from bson.objectid import ObjectId

class User(UserMixin):
    def __init__(self, email, nickname=None, db=False):
        self.email = email
        self.nickname = nickname
        if db:
            USERS_COLLECTION.insert_one({
                '_id': self.email, 'nickname': self.nickname,
                'friends': [], 'groups': []
                })

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.email

    def updateGroups(self, groupID):
        USERS_COLLECTION.find_one_and_update({
            '_id': ObjectId(groupID)}, {
            '$addToSet': {'groups': groupID}
        })
