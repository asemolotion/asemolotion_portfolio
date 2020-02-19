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
    return "バスで帰る"


def estimated_option(text):
    """
    textに近い話題のタイトルを返す関数

    Params:
        text: string: 送られてきた文字列
    Returns:
        string: 返信するメッセージ
    """
    return predict_reply(text)