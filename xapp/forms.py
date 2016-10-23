from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, IntegerField, DateField, SelectMultipleField, RadioField, FileField, FormField
from wtforms.validators import DataRequired, Email, Length
from xapp.models import USERS_COLLECTION, GROUPS_COLLECTION
from bson.objectid import ObjectId
from flask_login import current_user
import datetime


class LoginForm(FlaskForm):
    username = StringField('Email ID', description="Email", default="text", validators=[DataRequired(), Email()])
    phone = StringField('Mobile number', description="Phone", default="text",validators=[DataRequired()])
    password = PasswordField('Password', description="Password", default="password",validators=[DataRequired()])


class SignUpForm(FlaskForm):
    email = StringField('Email Address', [DataRequired(), Email(), Length(min=6, max=35)])
    name = TextField("First name", [DataRequired()])
    password = PasswordField('Password', [DataRequired(), Length(min=6)])


class FriendForm(FlaskForm):
    emailid = StringField('Email Address', [DataRequired(), Email(), Length(min=6, max=35)])


class GroupForm(FlaskForm):
    name = StringField(description='My Group' , validators=[DataRequired(), Length(max=25)])


'''
class GroupForm(FlaskForm):
    def __init__(self, userID):
        userFriends = (USERS_COLLECTION.find_one({'_id': userID}))['friends']
        users = SelectMultipleField('Select users to add to this group', choices=userFriends)
    name = StringField('My Group should be called as ...' , validators=[DataRequired(), Length(max=25)])
'''


class BillShare(FlaskForm):
    emailID = StringField('Add email id', validators=[DataRequired(), Email()])
    amount = IntegerField('Add amount', validators=[DataRequired()])


# not done paidfor
class BillForm(FlaskForm):
    topic = StringField('Topic', validators=[DataRequired(), Length(max=25)])
    amount = IntegerField('Amount', validators=[DataRequired()])
    currencies = []
    with open('xapp/currency.out', 'r') as f:
        for line in f:
            currencies.append(line)
    currency = RadioField('Currency', choices=currencies)
    tags = []
    with open('xapp/tags.out', 'r') as f:
        for line in f:
            tags.append(line)
    tag = RadioField('Tag', validators=[DataRequired()], default='Miscellaneous')
    date = DateField('Date', validators=[DataRequired()], default=datetime.datetime.utcnow())
    paidBy = FormField(BillShare)
    billShare = FormField(BillShare)
    billImage = FileField('Add your bill here')
