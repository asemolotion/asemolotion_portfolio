


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