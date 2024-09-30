# @time: 2022-10-18 16:02
# @author: 39295
from wtforms import Form
from app.libs.error_code import ParameterException
from flask import request


class BaseForm(Form):
    def __init__(self):
        data = request.form.to_dict()
        super(BaseForm, self).__init__(data=data)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ParameterException(msg=self.errors)
        return self