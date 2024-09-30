# @time: 2022-10-18 14:22
# @author: 39295
from app.web import web
from flask import request
from app.forms.auth import LoginForm, RegisterForm
from app.model.user import User
from app.model.base import db
from app.libs.error_code import Success, AuthError


@web.route('/login', methods=['POST', "GET"])
def login():
    form = LoginForm().validate_for_api()
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.password == form.password.data:
        return Success()
    else:
        raise AuthError(msg='邮箱未注册或参数错误')


@web.route('/register', methods=['POST', "GET"])
def register():
    form = RegisterForm().validate_for_api()
    user = User()
    user.set_attrs(form.data)
    db.session.add(user)
    db.auto_commit()
    return Success()
