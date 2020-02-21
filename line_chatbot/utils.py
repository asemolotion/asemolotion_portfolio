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
    返信Payloadを作成する関数。
    テキストによる返信か、カルーセルによる返信か、などの分岐はここ。

    Params:
        text: string: メッセージ
    Returns:
        payload: dict: 返信内容
    """

    # バス予定
    bus_schedule_words = ['バス','長崎','福岡']
    
    for word in bus_schedule_words:
        if word in text:
            reply_item = bus(text)
    
            payload = {
                "replyToken":reply_token,
            
                "messages":[
                        reply_item
                    ]
            }  
            return payload

    # メッセージ返信
    reply_message = message_reply(text)


    reply_item = {
        "type":"text",
        "text": reply_message
    }

    payload = {
        "replyToken":reply_token,
    
        "messages":[
                reply_item
            ]
    }      

    return payload

from .messages import *
def message_reply(text):
    """
    受け取ったメッセージごとに返信の文章を場合わけする関数

    Params:
        text: string: メッセージ
    Returns:
        reply_message: string: こちらからの返信
    """

    ##########################
    # 返信メッセージの条件分岐設定
    ##########################


    # 説明分
    if '使い方' in text:
        reply_message = instruction(text)

    # 返信推論
    else:
        reply_message = estimated_option(text)

    ##########################


    return reply_message