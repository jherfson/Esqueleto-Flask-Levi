from flask import Blueprint, render_template
from app import create_app

bp_index = Blueprint('index', __name__)
@bp_index.route('/')
def index():
    return render_template('index.html')
