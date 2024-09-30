# @time: 2022-10-18 14:40
# @author: 39295
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, DataRequired, Email, ValidationError
from app.model.user import User
from app.forms.base import BaseForm


class LoginForm(BaseForm):
    username = StringField(
        validators=[Length(min=2, max=30, message='用户名长度必须介于2-30之间'), DataRequired(message='数据不能为空')])
    password = StringField(
        validators=[Length(min=3, max=12, message='密码长度必须介于2-12之间'), DataRequired(message='密码不能为空，请输入密码')])
    # 验证数字
    # num = IntegerField(validators=[NumberRange(min=1, max=30)], default=1)
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])


class RegisterForm(BaseForm):
    username = StringField(
        validators=[Length(min=2, max=30, message='用户名长度必须介于2-30之间'), DataRequired(message='数据不能为空')])
    password = StringField(
        validators=[Length(min=3, max=12, message='密码长度必须介于2-12之间'), DataRequired(message='密码不能为空，请输入密码')])
    # 验证数字
    # num = IntegerField(validators=[NumberRange(min=1, max=30)], default=1)
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError(message='邮箱已被注册')

