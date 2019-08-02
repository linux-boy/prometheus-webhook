import requests
from dingtalk import messagebody
from config import setting
import json

def sendDingTalk(d_message):
    head = {"Content-Type": "application/json"}
    data = requests.post(url=setting.g_dingTalkHttpApi,data=json.dumps(d_message), headers=head)

if __name__ == '__main__':
    d={'markdown': {'title' : '2019-08-02T15:08:59.826409718+08:00',
                  'text': '#### ElasticSearch status \n'},
     'msgtype' : 'markdown'}

    d
    sendDingTalk(d)