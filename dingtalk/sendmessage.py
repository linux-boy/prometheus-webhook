import requests
from dingtalk import messagebody
from config import setting
import json

def sendDingTalk(d_message):
    head = {"Content-Type": "application/json"}
    data = requests.post(url=setting.g_dingTalkHttpApi,data=json.dumps(d_message), headers=head)

if __name__ == '__main__':
    sendDingTalk('test')