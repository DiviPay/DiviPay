from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, IntegerField, DateField, SelectMultipleField, RadioField, FileField
from wtforms.validators import DataRequired, Email, Length
from xapp.models import USERS_COLLECTION, GROUPS_COLLECTION
from bson.objectid import ObjectId
from flask_login import current_user
import datetime


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class SignUpForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=4, max=25)])
    email = StringField('Email Address', [DataRequired(), Email(), Length(min=6, max=35)])
    firstname = TextField("First name", [DataRequired()])
    lastname = TextField("Last name", [DataRequired()])
    password = PasswordField('Password', [DataRequired(), Length(min=6)])


class GroupForm(FlaskForm):
    name = StringField('My Group should be called as ...' , validators=[DataRequired(), Length(max=25)])


'''
class GroupForm(FlaskForm):
    def __init__(self, userID):
        userFriends = (USERS_COLLECTION.find_one({'_id': userID}))['friends']
        users = SelectMultipleField('Select users to add to this group', choices=userFriends)
    name = StringField('My Group should be called as ...' , validators=[DataRequired(), Length(max=25)])
'''
# not done paidfor
class BillForm(FlaskForm):
    def __init__(self, userID):
        groupUsers = (GROUPS_COLLECTION.find_one({'_id': userID}))['users']
        topic = StringField('Topic', validators=[DataRequired(), Length(max=25)])
        amount = IntegerField('Amount', validators=[DataRequired()])
        with open('currency.txt', 'r') as f:
            currencies = readline()
        print (currencies)
        currency = RadioField('Currency', choices=currencies)
        date = DateField('Date', validators=[DataRequired()], default=datetime.datetime.utcnow())
        paidBy = FormField(PaidBy)
        billImage = FileField('Add your bill here')

class PaidBy(FlaskForm):
    emailID = StringField('Add email id', validators=[DataRequired(), Email()])
    amount = IntegerField('Add amount', validators=[DataRequired()])
