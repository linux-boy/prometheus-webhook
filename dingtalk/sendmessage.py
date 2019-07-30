import requests
from dingtalk import messagebody
from config import setting
import json

def sendDingTalk(d_message):
    d_dtmessage = messagebody.dingMarkDown('test', 'test', ['18898692781'],'test')
    head = {"Content-Type": "application/json"}
    data = requests.post(url=setting.g_dingTalkHttpApi,data=json.dumps(d_dtmessage), headers=head)

if __name__ == '__main__':
    sendDingTalk('test')