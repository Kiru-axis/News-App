from flask import render_template
from . import main
# from app import main

@main.errorhandler(404)
def four_Ow_four(err):
    """
    Function to render the 404 error page
    """
    return render_template('fourOwfour.html'),404
