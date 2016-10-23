from bson.objectid import ObjectId
from xapp.models import GROUPS_COLLECTION, BILLS_COLLECTION
from xapp.simplify import Simplify
from flask_login import current_user
import datetime


class AddGroup(object):
    def __init__(self, name, users=None, bills=None, timestamp=None, graph=None):
        self.name = name
        self.timestamp = datetime.datetime.utcnow()
        self.users = users
        self.users.append(current_user.get_id())
        self.bills = []
        self.graph = graph

    def addGroup(self):
        GROUP_ID = GROUPS_COLLECTION.insert_one({
            'name': self.name, 'timestamp': self.timestamp,
            'members': self.users, 'graph': self.graph
        }).inserted_id
        return GROUP_ID


class Group(object):
    def __init__(self, groupID):
        self.groupID = groupID

    def addUsers(self, users):
        GROUPS_COLLECTION.find_one_and_update({
            '_id': ObjectId(self.groupID)}, {
                '$addToSet': {'users': users}
            })

    def addBill(self, billID):
        GROUPS_COLLECTION.find_one_and_update({
            '_id': ObjectId(self.groupID)}, {
                'addToSet': {'bills': billID}
            })
        bill = BILLS_COLLECTION.find_one({'_id': ObjectId(billID)})
        graph = GROUPS_COLLECTION.find_one({'_id': ObjectId(self.groupID)})['graph']
        paid_for = [[key, value] for key, value in bill['billShare'].items()]
        ind = 0
        for key, value in bill['paidBy'].items():
            entry = dict()
            entry['lender'] = value
            while ind < len(paid_for):
                entry['borrower'] = paid_for[ind][0]
                if value >= paid_for[ind][1]:
                    value -= paid_for[ind][1]
                    entry['amount'] = paid_for[ind][1]
                    paid_for[ind][1] = 0
                    ind += 1
                else:
                    paid_for[ind][1] -= value
                    entry['amount'] = value
                    graph.append(entry)
                    break
                graph.append(entry)
        GROUPS_COLLECTION.find_one_and_update({
            '_id': ObjectId(self.groupID)}, {
                'addToSet': {'graph': graph}
            })

    def simplify(self):
        grp = GROUPS_COLLECTION.find_one({'_id': ObjectId(self.groupID)})
        smp = Simplify(grp['graph'], grp['users'])
        graph = smp.calculate()
        GROUPS_COLLECTION.find_one_and_update({
            '_id': ObjectId(self.groupID)}, {
                'addToSet': {'graph': graph}
            })

