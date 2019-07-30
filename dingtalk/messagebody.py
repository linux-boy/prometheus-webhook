def dingText(s_content, l_mobiles, b_isAtAll):
    return {"msgtype" : "text",
            "text": {
                "content": s_content
            },
            "at": {
                "atMobiles":l_mobiles,
                "isAtAll": b_isAtAll
            }
    }

def dingLink(s_content, s_title, s_picUrl, s_messageUrl):
    return {
        "msgtype" : "link",
        "link" : {
            "text" : s_content,
            "title" : s_title,
            "picUrl" : s_picUrl,
            "messageUrl" : s_messageUrl
        }
    }

def dingMarkDown(s_titile, s_content, l_mobiles, b_isAtALL):
    return {
        "msgtype": "markdown",
        "markdown": {
            "title" : s_titile ,
            "text" : s_content
        },
        "at" : {
            "atMobiles" : l_mobiles,
            "isAtAll": b_isAtALL
        }
    }
