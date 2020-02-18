import json

from .conf_vars import REPLY_ENDPOINT, CHANNEL_ACCESS_TOKEN
import urllib.request
import urllib.parse

import requests

def parse_line_webhook(request):
    """
    LINEのwebhookからのリクエストを分解して、
    返信に必要なメッセージとreply_tokenを取り出し、
    メッセージがある時に、返信する関数reply を呼びだす関数。

    Params:
        request: Django Request object

    Returns:
        None
    """
    request_json = json.loads(request.body.decode('utf-8'))

    if request_json != None:  # requestの中身が何かあるとき

        for event in request_json['events']:  # スタンプとメッセージみたいに複数が来ることもある

            reply_token = event['replyToken'] # 返信に必要なID
            
            event_type = event['type']

            if event_type == 'message':  # スタンプもmessageなので注意。
                text = event['message'].get('text', None)  # message['type']が'sticker'の場合は'text'のデータは入っていない。

                if text:  # 文章があった場合、返信。
                    reply(reply_token, text)
    
    else:  # 何もない時。
        pass

    return 


def reply(reply_token, text):
    """
    受け取ったメッセージから返信する内容を作り、実際にLINE APIを通じて返信をする関数

    Params:
        reply_token, text: (string, string): 

    Returns:
        None    
    """

    payload = dispatch_payload(reply_token, text)

    header = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + CHANNEL_ACCESS_TOKEN  # チャンネルアクセストークン
	}

    requests.post(REPLY_ENDPOINT, headers=header, data=json.dumps(payload))

    return 'replied'

from .messages import *

def dispatch_payload(reply_token, text):
    """
    受け取ったメッセージごとに返信を場合わけする関数

    Params:
        text: string: メッセージ
    Returns:
        payload: dict: 返信内容
    """
    
    if 'バス' in text:
        my_message = bus(text)
    else:
        my_message = echo(text)

    payload = {
        "replyToken":reply_token,
        "messages":[
                {
                    "type":"text",
                    "text": my_message
                }
            ]
        }  

    return payload

