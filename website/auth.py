from xmlrpc.client import boolean
from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/', methods=['GET','POST'])
def base():
    return render_template('base.html')

