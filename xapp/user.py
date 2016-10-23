from werkzeug.security import check_password_hash, generate_password_hash
from xapp.models import USERS_COLLECTION
from flask_login import UserMixin
from bson.objectid import ObjectId

class User(UserMixin):
    def __init__(self, username, email=None, firstname=None, lastname=None, password=None, db=False):
        self.username = username
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.password = password
        if db:
            USERS_COLLECTION.insert_one({
                '_id': self.username, 'email': self.email,
                'firstname': self.firstname, 'lastname': self.lastname,
                'password': generate_password_hash(self.password),
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
        return self.username

    @staticmethod
    def validate_login(password_hash, password):
        return check_password_hash(password_hash, password)

    def updateGroups(self, groupID):
        USERS_COLLECTION.find_one_and_update({
            '_id': ObjectId(groupID)}, {
            '$addToSet': {'groups': groupID}
        })
