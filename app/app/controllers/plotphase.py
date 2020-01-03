from flask import Blueprint, render_template
from app import create_app

bp_plotphase = Blueprint('plotphase', __name__)
@bp_plotphase.route('/plotphase')
def plotphase():
    return render_template('plotphase.html')
