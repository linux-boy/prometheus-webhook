from flask import Flask, request
import json
from config import setting
from flask import templating
from dingtalk import messagebody
from config import setting
app = Flask(__name__)

@app.route("/dtwebhook", methods=['POST'])
def sendMessageToDingTalk():
    d_data = json.loads(request.data)
    



def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

if __name__ == '__main__':
    app.after_request(after_request)
    app.run(port=setting.g_flaskPort, debug=False)