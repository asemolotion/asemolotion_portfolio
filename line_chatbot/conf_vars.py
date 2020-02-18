"""

LINE APIを使う上での、キーなど。
line_chatbotアプリでしか使わない変数を設定しているモジュール。

"""


import socket 

hostname = socket.gethostname()
if 'local' in hostname:
    from conf.local_settings import LINE_REPLY_ENDPOINT as REPLY_ENDPOINT
    from conf.local_settings import LINE_CHANNEL_ACCESS_TOKEN as CHANNEL_ACCESS_TOKEN
    
    REPLY_ENDPOINT = REPLY_ENDPOINT
    CHANNEL_ACCESS_TOKEN = CHANNEL_ACCESS_TOKEN

else:
    import os
    REPLY_ENDPOINT = os.environ.get('LINE_REPLY_ENDPOINT')
    CHANNEL_ACCESS_TOKEN = os.environ.get('LINE_CHANNEL_ACCESS_TOKEN')