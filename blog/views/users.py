from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

users_app = Blueprint('users_app', __name__)
USERS = {
    1: 'John',
    2: 'Brian',
    3: 'Bob',
    4: 'balodia'
}


@users_app.route('/', endpoint='list')
def user_list():
    return render_template('users/list.html', users=USERS)
