from flask import Flask, request, abort

import os

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import  InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageAction

import datetime

import openpyxl as px
from random import randint

app = Flask(__name__)

#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/")
def hello_world():
    return "hello what your name?"

@app.route("/kaito")
def aho():
    return str(10+20)


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
    plan=1
    yyyy=2
    MM=3
    dd=4
    hh=5
    mm=6
    issue_id_col=9
    flag=10#列の名前のflag
    buffer1=11
    buffer2=12
    buffer3=13
    error_catch=14

    Flag=0#条件分岐のためのflag
    issue_id=randint(0,1000)
    wb=px.load_workbook("sample1.xlsx")#open xls file(wb=work book)
    ws = wb["plan"]#get sheet data(ws=work sheet)
    wb_w=px.load_workbook("sample1.xlsx")
    ws_w=wb_w.worksheets[0]
    Flag=int(ws.cell(row=2,column=flag).value)

    if int(ws.cell(row=2,column=error_catch).value)==1:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="error occured!\nplease try again at start!!"),
        )
        ws_w.cell(row=2,column=flag,value=0)

    else:
        if Flag==0:
            if event.message.text == "予約":
                line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="予約を行います日付を教えてください\nex)明日、今日、明後日、11月6日"),               
            )
                ws_w.cell(row=2,column=flag,value=1)
            else:
                line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="予約したいときは”予約と入力してください”"),
            )
                ws_w.cell(row=2,column=flag,value=0)

        elif Flag==1:
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="何時何分に設定しますか\n入力フォーマット例(11時11分のとき):11:11（半角）"),
            )
            ws_w.cell(row=2,column=flag,value=2)
            ws_w.cell(row=issue_id,column=buffer1,value=event.message.text)

        elif Flag==2:
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="何の予定がありますか？"),
            )
            ws_w.cell(row=2,column=buffer2,value=event.message.text)

        elif Flag == 3:
            line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="予約を完了しました"),        
           )
            ws_w.cell(row=2,column=buffer3,value=event.message.text)
            ws_w.cell(row=2,column=flag,value=0) 
    
    wb_w.save("sample1.xlsx")

     



#error時の対応

#sample bot
"""
    profile = line_bot_api.get_profile(event.source.user_id)

    status_msg = profile.status_message
    if status_msg != "None":
        # LINEに登録されているstatus_messageが空の場合は、"なし"という文字列を代わりの値とする
        status_msg = "なし"

    messages = TemplateSendMessage(alt_text="Buttons template",
                                   template=ButtonsTemplate(
                                       thumbnail_image_url=profile.picture_url,
                                       title=profile.display_name,
                                       text=f"User Id: {profile.user_id[:8]}...\n"
                                            f"Status Message: {status_msg}",
                                       actions=[MessageAction(label="成功", text="次は何を実装しましょうか？")]))

    line_bot_api.reply_message(event.reply_token, messages=messages)
"""


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)