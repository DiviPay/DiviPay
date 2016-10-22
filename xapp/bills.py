from xapp.models import BILLS_COLLECTION
import datetime


class AddBill():
    def __init__(self, topic, amount, currency=None, paidBy=None, billShare=None, tag=None, datetime=None):
        self.topic = topic
        self.amount = amount
        self.currency = currency
        self.paidBy = paidBy
        self.billShare = billShare
        self.tag = tag
        self.datetime = datetime.datetime.utcnow()

    def addBill(self):
        billID = BILLS_COLLECTION.insert_one({
                    'topic': self.topic, 'amount': self.amount, 'currency': self.currency,
                    'paidBy': self.paidBy, 'billShare': self.billShare, 'tag': self.tag,
                    'datetime': self.datetime
            }).inserted_id
        return billID


class Bill():
    def __init__(self, billID):
        self.billID = billID

    def addTopic(self, topic):
        BILLS_COLLECTION.find_one_and_update({'_id': self.billID}, {'$set': {'topic': topic}})

    def addAmount(self, amount):
        BILLS_COLLECTION.find_one_and_update({'_id': self.billID}, {'$set': {'amount': amount}})

    def addCurrency(self, currency):
        BILLS_COLLECTION.find_one_and_update({'_id': self.billID}, {'$set': {'currency': currency}})

    def addPaidBy(self, paidbyShare):
        BILLS_COLLECTION.find_one_and_update({'_id': self.billID}, {'$set': {'paidBy': paidBy}})

    def addbillShare(self, billShare):
        BILLS_COLLECTION.find_one_and_update({'_id': self.billID}, {'$set': {'billShare': billShare}})

    def addTag(self, tag):
        BILLS_COLLECTION.find_one_and_update({'_id': self.billID}, {'$set': {'tag': tag}})
