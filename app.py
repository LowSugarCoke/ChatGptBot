from __future__ import unicode_literals
import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import configparser
import random
import chatgpt


app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi('Ewc+QCUEzYADuool1mgR8hj8SmOdmnoi96qtBraPQC6Ke+JktMYDW4Pz7R2lE6PyUh2wuSao6F1nxprSB8Dgq4bzJQVsfJc9M8OheR3+m6FAV9lfjaDiG3WU3PdhErVWLAhHVMKa4ODXN5UL8ySMjAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3a1c2d841e01faa8bf1e8a32b0a0a171')


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 學你說話
@handler.add(MessageEvent, message=TextMessage)
def pretty_echo(event):
    
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=chatgpt.askChatGpt(event.message.text))
        )

if __name__ == "__main__":
    app.run()