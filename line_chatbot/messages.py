from line_chatbot.reply_prediction.main import predict_reply


def echo(text):
    """
    おうむ返しの返信を作る関数。

    Params:
        text: string: 送られてきた文字列
    Returns:
        string: 返信するメッセージ
    """
    return "%s です。" % text

def bus(text):
    """
    バス専用の返信を作る関数。

    Params:
        text: string: 送られてきた文字列
    Returns:
        string: 返信するメッセージ
    """
    reply_item = {
  			"type": "template",
  			"altText": "this is a confirm template",
  			"template": {
  				"type": "carousel",
  				"columns":[
  					{
  						"title": "長崎福岡間のバスの時刻表",
  						"text":"選択してください",
  						"actions": [
  							{
  								"type":"uri",
  								"label":"長崎から福岡",
  								"uri": "https://www.navitime.co.jp/highwaybus/42_40"
  							},
  							{
  								"type": "uri",
  								"label": "福岡から長崎",
  								"uri":"https://www.navitime.co.jp/highwaybus/40_42"
  							},
  						]
  					}
  				]
  			}
  		}    
    
    return reply_item


def estimated_option(text):
    """
    textに近い話題のタイトルを返す関数

    Params:
        text: string: 送られてきた文字列
    Returns:
        string: 返信するメッセージ
    """
    return predict_reply(text)

def instruction(text):
    """
    使い方メッセージを返す関数

    Params:
        text: string: 送られてきた文字列
    Returns:
        string: 返信するメッセージ
    """
    instruction_message = """
    
    これはasemolotionのポートフォリオ用のラインアカウントです。
    
    ＊＊＊＊
    
    使い方①
    「バス」、「長崎」、「福岡」、のどれかの文字を含むメッセージを送ったら
    長崎福岡のバスのスケジュールが返される。

    使い方②
    「使い方」という文字を送ればこの説明文が返ってくる。

    使い方③
    その他のメッセージでは自治体アカウントのような項目を予測して返す。
    ※サーバの具合で推論に時間がかかったり返信がこない場合があります。

    """

    return instruction_message
