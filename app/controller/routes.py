from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from config import Config


routes_blueprint = Blueprint('routes', __name__)
routes_blueprint.template_folder = Config.TEMPLATE_FOLDER

@routes_blueprint.route('/')
def index():
    return render_template('base.html', title='Home')

@routes_blueprint.route('/main')
def mainpage():
    return render_template('mainpage.html', title='Mainpage')


