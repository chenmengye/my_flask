# @time: 2022-10-15 17:13
# @author: 39295
from app.libs.error import APIException


class AuthError(APIException):
    # 请求参数错误
    code = 444
    error_code = 999
    description = '请求参数错误'


class ParameterException(APIException):
    code = 400
    msg = '参数验证失败'
    error_code = 111


class Success(APIException):
    code = 201
    msg = 'ok'
    error_code = 0


class ServerError(APIException):
    code = 500
    msg = '出错啦'
    error_code = 999