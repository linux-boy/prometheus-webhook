from flask import Flask, request
import json
from config import setting
from flask import templating
from dingtalk import messagebody
from dingtalk import sendmessage
from config import setting
app = Flask(__name__)

@app.route("/dtwebhook", methods=['POST'])
def sendMessageToDingTalk():
    d_data = json.loads(request.data.decode())
    s_title = d_data['annotations']['description']
    s_startsAt = d_data['startsAt']
    s_endsAt = d_data['endsAt']
    s_text = ''
    for b_text in d_data['alerts']:
        s_title = s_title +'['+ b_text['labels']['cluster']+']'+'('+b_text['labels']['generatorURL']+')'
    d_body = messagebody.dingMarkDown(s_title=s_title, s_content=s_startsAt+'\n'+s_endsAt+'\n'+s_text)
    sendmessage(d_body)
    return '200'
    



def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

if __name__ == '__main__':
    app.after_request(after_request)
    app.run(port=setting.g_flaskPort, debug=False)