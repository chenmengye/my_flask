# @time: 2022-10-15 16:43
# @author: 39295
import json
import requests


def request_post():
    param = {'a': 11}
    url = 'http://10.32.23.119:5000/test'
    ret = requests.post(url, data=param)
    print(json.loads(ret.text))


request_post()