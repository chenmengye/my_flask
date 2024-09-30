# @time: 2022-10-15 17:31
# @author: 39295
from flask import request
from itsdangerous import json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg = '未知错误'
    error_code = 999

    def __init__(self, msg=None, code=None, error_code=None, headers=None):
        if code:
            self.code = code
        if msg:
            self.msg = msg
        if error_code:
            self.error_code = error_code
        super(APIException, self).__init__()

    def get_body(self, environ=None, scope=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + ' ' + self.get_url_para()
        )
        return json.dumps(body)

    def get_headers(self, environ=None, scope=None):
        return [('Content-Type', 'application/json')]

    @staticmethod
    def get_url_para():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

