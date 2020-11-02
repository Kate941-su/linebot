from flask import Flask, request, abort

import os

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import  InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageAction

import datetime

app = Flask(__name__)

#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello what your name?"

#Webhook設定
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#kokoまでは同じ

##メッセージ受信時
"""
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text2=event.message.text
    line_bot_api.reply_message(
        event.reply_token,
#        TextSendMessage(text=event.message.text)
        TextSendMessage(text=text2),
        )
"""

@handler.add(MessageEvent, message=TextMessage)
def response_message(event):
    profile = line_bot_api.get_profile(event.source.user_id)

    status_msg = profile.status_message
    if status_msg != "None":
        # LINEに登録されているstatus_messageが空の場合は、"なし"という文字列を代わりの値とする
        status_msg = "なし"

    messages = TemplateSendMessage(alt_text="Buttons template",
                                   template=ButtonsTemplate(
                                       thumbnail_image_url=profile.picture_url,
                                       title=profile.display_name,
                                       text=f"User Id: {profile.user_id}...\n"
                                            f"Status Message: {status_msg}",
                                       actions=[MessageAction(label="成功", text="次は何を実装しましょうか？")]))
    line_bot_api.reply_message(event.reply_token, messages=messages)


"""
@handler.add(MessageEvent,message=TextMessage)
def push_message(event):   
    line_bot_api.push_message("<to>",TextMessage(text="helloworld"))
""" 


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)