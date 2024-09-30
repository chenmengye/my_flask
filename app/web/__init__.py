# @time: 2022-10-18 14:30
# @author: 39295
from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import auth
