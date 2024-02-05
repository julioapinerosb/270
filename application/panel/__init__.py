from flask import Flask, render_template, url_for, request, make_response, redirect, Response, Blueprint


panel = Blueprint('panel', __name__, template_folder='templates')

from . import routes