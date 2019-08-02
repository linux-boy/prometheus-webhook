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
    # print(request.data)
    d_data = json.loads(request.data.decode())
    # print(d_data)
    s_title = d_data['alerts'][0]['annotations']['description']
    s_text = ''
    for b_text in d_data['alerts']:
        s_startsAt = b_text['startsAt']
        s_endsAt = b_text['endsAt']
        s_text = s_text +' #### ['+ b_text['labels']['cluster']+']'+'('+b_text['generatorURL']+')'

    d_body = messagebody.dingMarkDown(s_title=s_title, s_content=s_startsAt+'\n'+s_text)
    # print(d_body)
    sendmessage.sendDingTalk(d_body)
    return '200'
    



def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

if __name__ == '__main__':
    app.after_request(after_request)
    app.run(port=setting.g_flaskPort, debug=False)