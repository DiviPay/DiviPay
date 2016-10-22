from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, SelectMultipleField, RadioField, FileField
from wtforms.validators import DataRequired, Email, Length
from xapp.models import USERS_COLLECTION, GROUPS_COLLECTION
from bson.objectid import ObjectId
from flask_login import current_user
import datetime


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

'''
class SignUpForm(FlaskForm):
    username = StringField('Username', [DataRequired(), Length(min=4, max=25)])
    email = StringField('Email Address', [DataRequired(), Email(), Length(min=6, max=35)])
    firstname = TextField("First name", [DataRequired()])
    lastname = TextField("Last name", [DataRequired()])
    password = PasswordField('Password', [DataRequired(), Length(min=6)])
'''

class GroupForm(FlaskForm):
    userID = current_user.get_id()
    userFriends = (USERS_COLLECTION.find_one({'_id': ObjectId(userID)}))['friends']
    name = StringField('My Group should be called as ...' , validators=[DataRequired(), Length(max=25)])
    users = SelectMultipleField('Select users to add to this group', choices=groupUsers)


class BillForm(FlaskForm):
    userID = current_user.get_id()
    groupUsers = (GROUPS_COLLECTION.find_one({'_id': ObjectId(userID)}))['users']
    topic = StringField('Topic', validators=[DataRequired(), Length(max=25)])
    amount = IntegerField('Amount', validators=[DataRequired()])
    ########## check
    with open('currency.txt', 'r') as f:
        currencies = readline()
    currency = RadioField('Currency', choices=currencies)
    date = DateField('Date', validators=[DateRequired()], default=datetime.datetime.utcnow())
    paidBy = PaidBy()
    billImage = FileField('Add your bill here')


class PaidBy(FlaskForm):
    emailID = StringField('Add email id', validators=[DataRequired(), Email()])
    amount = IntegerField('Add amount', validators=[DataRequired()])
