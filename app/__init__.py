# @time: 2022-10-18 14:32
# @author: 39295
from app.web.auth import web
from flask import Flask
from app.model.base import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    app.register_blueprint(web, url_prefix='/admin')
    db.init_app(app)
    db.create_all(app=app)
    return app