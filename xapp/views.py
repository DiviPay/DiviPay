from xapp.application import app, lm
from xapp.forms import GroupForm, LoginForm, SignUpForm, BillForm
import pymongo
from groups import AddGroup, Group
from flask import request, redirect, render_template, url_for, flash, session
from flask_login import login_user, logout_user, login_required, current_user
from xapp.models import USERS_COLLECTION, GROUPS_COLLECTION, BILLS_COLLECTION, TRANSACTION_COLLECTION
from xapp.user import User
from bson.objectid import ObjectId


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = USERS_COLLECTION.find_one({"_id": form.username.data})
        if user and User.validate_login(user['password'], form.password.data):
            user_obj = User(user['_id'])
            login_user(user_obj, remember=True)
            flash("Logged in successfully!", category='success')
            #return redirect(url_for(''))
        flash("Wrong username or password!", category='error')
    print(current_user.get_id())
    return render_template('login1.html', title='DiviPay | Login', form=form)
    # login1.html kara hai


@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = USERS_COLLECTION.find_one({'email': form.email.data})
        if user:
            flash("You have already signed up from this email id", category='error')
        else:
            user = USERS_COLLECTION.find_one({'_id': form.username.data})
            if user:
                flash("That username has already been taken", category='error')
            else:
                User(form.username.data, form.email.data, form.firstname.data,
                     form.lastname.data, form.password.data, db=True)
                flash("SignUp successfull!", category='success')
                return redirect(url_for('login'))
    return render_template('signup.html', title='HoverSpace | Signup', form=form)


@app.route('/logout/')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/addgroup/', methods=['GET', 'POST'])
def addGroup():
    userID = current_user.get_id()
    form = GroupForm()
    userFriends = (USERS_COLLECTION.find_one({'_id': userID}))['friends']
    if request.method == 'POST':
        group = AddGroup(form.name.data, form.users.data)
        groupID = group.addGroup()
        usr = User(userID)
        usr.updateGroups(groupID)
        return redirect(url_for('viewGroup', groupID=groupID))
    return render_template('addgroup.html', form=form, friends=userFriends)


@app.route('/groups/<groupID>/', methods=['GET'])
def viewGroup(groupID):
    return render_template('groups.html', groupID=groupID)

@app.route('/groups/<groupID>/simplify', methods=['GET'])
def simplification(groupID):
    grp = Group(groupID)
    grp.simplify()
    return redirect(url_for('viewGroup', groupID=groupID))

@app.route('/addBill/', methods=['GET', 'POST'])
def addBill():
    userID = current_user.get_id()
    form = BillForm(userID)
    if request.method == 'POST':
        pass
    return render_template('addBill.html', form=form)


@lm.user_loader
def load_user(username):
    user = USERS_COLLECTION.find_one({'_id': username})
    if not user:
        return None
    return User(user['_id'])
