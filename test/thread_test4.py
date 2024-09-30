# @time: 2022-10-15 15:56
# @author: 39295
import time

from flask import Flask, request,jsonify


app = Flask(__name__)


@app.route('/test', methods=['POST'])
def test():
    a = int(request.form.get('a'))
    a = a + 1
    time.sleep(10)
    return jsonify(a)


app.run(host='0.0.0.0', debug=app.config['DEBUG'])
