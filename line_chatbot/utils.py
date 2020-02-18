import json
from .conf_vars import REPLY_ENDPOINT, CHANNEL_ACCESS_TOKEN
import urllib.request

def parse_line_webhook(request):
    """
    LINEのwebhookからのリクエストを分解して、
    返信に必要なメッセージとreply_tokenを取り出す関数。

    Params:
        request: Django Request object

    Returns:
        (replytoken, text): (string, string)
    """
    request_json = json.loads(request.body.decode('utf-8'))

    
    print(request_json)

    if(request_json != None):  # requestの中身が何かあるとき

        for event in request_json['events']:
            # maybe one event comes...
            reply_token = event['replyToken'] # important
            event_type = event['type']

            if event_type == 'message':
                text = event['message']['text']
    else:
        reply_token = 'No reply_token'
        text = 'No text'

    return reply_token, text


def reply(reply_token, text):
    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + CHANNEL_ACCESS_TOKEN  # チャンネルアクセストークン
	}
    payload = {
        "replyToken":reply_token,
        "messages":[
                {
                    "type":"text",
                    "text": "%s です。" % text
                }
            ]
        }
    # requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))
    urllib.request.Request(REPLY_ENDPOINT, payload, headers)
    
    return 
    