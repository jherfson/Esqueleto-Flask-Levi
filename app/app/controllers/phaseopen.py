from flask import Blueprint, render_template
from app import create_app

bp_phaseopen = Blueprint('phaseopen', __name__)
@bp_phaseopen.route('/phaseopen')
def phaseopen():
    return render_template('phaseopen.html')
