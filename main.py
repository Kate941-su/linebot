from flask import Flask, request, abort

import os,re

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import  InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageAction

from datetime import datetime

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
#each column
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
    mistake=15
    send_id=16
    bffer_id=17

#buffering_row
    b_row=201

#入力ミス防止    
    error_flag=0
    Flag=0#条件分岐のためのflag
    pattern = r'(0?[1-9]|1[0-2])[/\-月](0?[1-9]|[12][0-9]|3[01])日?$'#日付一致の正規表現
    profile = line_bot_api.get_profile(event.source.user_id)
    User_id=profile.user_id
    this_year=2020
#fileの有無　あればそれを開くなければつくってそれを開く
    if os.path.exists("./user"+str(User_id)+".xlsx"):
        wb=px.load_workbook("./user"+str(User_id)+".xlsx")#open xls file(wb=work book)
        ws = wb["plan"]#get sheet data(ws=work sheet)
        wb_w=px.load_workbook("./user"+str(User_id)+".xlsx")
        ws_w=wb_w.worksheets[0]
        ws_w.cell(row=b_row,column=send_id,value=User_id)
        wb_w.save("./user"+str(User_id)+".xlsx")
        wb=px.load_workbook("user"+str(User_id)+".xlsx")#open xls file(wb=work book)
        ws = wb["plan"]#get sheet data(ws=work sheet)
        Flag=int(ws.cell(row=b_row,column=flag).value)
        Mistake=int(ws.cell(row=b_row,column=mistake).value)
  
        if int(ws.cell(row=b_row,column=mistake).value)==2:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="try again at first!!"),
            )
            ws_w.cell(row=b_row,column=mistake,value=0)
            ws_w.cell(row=b_row,column=flag,value=0)
    
    #Flag1 phase

        else:
            if Flag==0:
                if event.message.text == "予約":
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="予約を行います日付を教えてください\nex)明日、今日、明後日、11月6日\n※予約時刻は10分単位で行います1分単位で予約すると10分繰り上げ通知となります"),               
                )
                    ws_w.cell(row=b_row,column=flag,value=1)
                else:
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="予約したいときは”予約と入力してください”"),
                )
                    ws_w.cell(row=b_row,column=flag,value=0)

            elif Flag==1:

                is_message_date = event.message.text
                ws_w.cell(row=b_row,column=buffer1,value=is_message_date)
                wb_w.save("user"+str(User_id)+".xlsx")
                wb=px.load_workbook("user"+str(User_id)+".xlsx")#open xls file(wb=work book)
                ws = wb["plan"]#get sheet data(ws=work sheet)
                #型を判定する
                #datetime型で方が一致していた時
                if str(ws.cell(row=b_row,column=buffer1).value) == "今日":   
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="何時何分に設定しますか\n入力フォーマット例(11時00分のとき):11:00（半角）\n※10分単位です!"),
                    )
                    ws_w.cell(row=b_row,column=flag,value=2)
                    ws_w.cell(row=b_row,column=buffer1,value=event.message.text)#issue id

                elif str(ws.cell(row=b_row,column=buffer1).value) == "明日":   
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="何時何分に設定しますか\n入力フォーマット例(11時10分のとき):11:10（半角）"),
                    )
                    ws_w.cell(row=b_row,column=flag,value=2)
                    ws_w.cell(row=b_row,column=buffer1,value=event.message.text)#issue id

                elif str(ws.cell(row=b_row,column=buffer1).value) == "明後日":   
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="何時何分に設定しますか\n入力フォーマット例(11時10分のとき):11:10（半角）"),
                    )
                    ws_w.cell(row=b_row,column=flag,value=2)
                    ws_w.cell(row=b_row,column=buffer1,value=event.message.text)#issue id

                    #今日明日明後日意外の処理
                else:
                    
                    if bool(re.match(pattern,ws.cell(row=b_row,column=buffer1).value)):
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="何時何分に設定しますか\n入力フォーマット例(11時10分のとき):11:10（半角）\n"),
                        )
                        ws_w.cell(row=b_row,column=flag,value=2)
                        ws_w.cell(row=b_row,column=buffer1,value=event.message.text)#issue id
                
                    else:
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="入力ミスがあります。このような間違えはありませんか？\n数字が半角、月日をどちらか抜かしている")
                        ),
                        ws_w.cell(row=b_row,column=flag,value=1)
                        ws_w.cell(row=b_row,column=mistake,value=Mistake+1)

    #Flag2 phase

            elif Flag==2:
                r_message=event.message.text           
                try:
                    k=0
                    r_message=r_message.split(":")
                    for i in r_message:
                        r_message[k]=int(i)
                        k+=1
                    if r_message[0]>=25 or r_message[1]>=60:
                        error_flag=1
                except:
                    error_flag=1


                if error_flag == 0:    
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="何の予定がありますか？\n"),
                    )
                    ws_w.cell(row=b_row,column=flag,value=3)
                    ws_w.cell(row=b_row,column=buffer2,value=event.message.text)#issue id

                else:
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="入力ミスがあります。\n何時何分に設定しますか\n入力フォーマット例(11時10分のとき):11:10（半角）"),
                    )
                    ws_w.cell(row=b_row,column=flag,value=2)
    #               ws_w.cell(row=b_row,column=buffer1,value=event.message.text)
                    ws_w.cell(row=b_row,column=mistake,value=Mistake+1)
    #Flag3 phase

            elif Flag == 3:
                ws_w.cell(row=b_row,column=buffer3,value=event.message.text)#issue id
                ws_w.cell(row=b_row,column=flag,value=0)
                ws_w.cell(row=b_row,column=send_id,value=profile.user_id)
                wb_w.save("user"+str(User_id)+".xlsx")
                wb=px.load_workbook("user"+str(User_id)+".xlsx")#open xls file(wb=work book)
                ws = wb["plan"]#get sheet data(ws=work sheet)

                k=0
                while k<=200:
                    k+=1
                    issue_id=randint(2,200)
                    if ws.cell(row=issue_id,column=issue_id_col) == None:
                        ws_w.cell(row=issue_id,column=buffer3,value=ws.cell(row=b_row,column=buffer3).value)
                        ws_w.cell(row=issue_id,column=buffer1,value=ws.cell(row=b_row,column=buffer1).value)
                        ws_w.cell(row=issue_id,column=buffer2,value=ws.cell(row=b_row,column=buffer2).value)
                        if type(ws.cell(row=b_row,column=buffer1).value) != type("helloworld"):
                            if datetime.now()>datetime(year=this_year,month=ws.cell(row=b_row,column=buffer1).value.month,day=ws.cell(row=b_row,column=buffer1).value.day):
                                ws_w.cell(row=issue_id,column=yyyy,value=this_year+1)
                        break
               
                if k == 200:
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="予約件数は200までです。"),        
                    )
                    
                else:
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=str(ws.cell(row=b_row,column=buffer1).value)+str(ws.cell(row=b_row,column=buffer2).value)+"に"+"”"+str(ws.cell(row=b_row,column=buffer3).value)+"”"+"で予約しました。\n"),        
            )




    #            ws_w.cell(row=b_row,column=buffer3,value=event.message.text)#issue id
    #            ws_w.cell(row=b_row,column=flag,value=0) 
        
        wb_w.save("user"+str(User_id)+".xlsx")

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="登録までお待ちください"),
        ) 
        user_id = os.environ["MY_ID"]
        line_bot_api.push_message(user_id, TextSendMessage(text=str(datetime.now().month)+"月"+str(datetime.now().day)+"日\n"+str(user_id)+"さんが登録を要請しました。\nファイルの作成をしてください。\nファイル名"+str(user_id)+".xlsx")
        )



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