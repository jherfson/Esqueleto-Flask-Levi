from flask import Blueprint, render_template
from app import create_app

bp_phasediagram = Blueprint('phasediagram', __name__)
@bp_phasediagram.route('/phasediagram')
def phasediagram():
    return render_template('phasegiagram.html')
