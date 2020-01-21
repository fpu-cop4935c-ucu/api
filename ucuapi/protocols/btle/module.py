from flask import Blueprint

btle = Blueprint('btle', __name__)

@btle.route('/test')
def btle_main():
    return "Main"
