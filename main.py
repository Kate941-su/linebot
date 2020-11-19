from flask import Flask, request, abort

import os,re

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import  InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageAction

from datetime import datetime

import openpyxl as px
from random import randint

import psycopg2 as p2

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

#connect heroku postgresql
    connection = p2.connect("host=ec2-3-213-106-122.compute-1.amazonaws.com port=5432 dbname=dap1bs8ml5o18m user=lenlmwyicflwcu password=a6d1cfd820fd5146b52ebf39c8a6bde0d5e71e1ec5b12fd85307ecb43ccf928d")
    connection.autocommit = True
    #これによってSQLオブジェクトを使用可能にする
    cur = connection.cursor()
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
    buffer_date=18
    true_date=19
    true_time=20
    b_month=21
    b_day=22
    b_hour=23
    b_minute=24
#buffering_row
    b_row=201


    list30=[4,6,9,11]
    list31=[1,3,5,7,8,10,12]

#入力ミス防止    
    error_flag=0
    Flag=0#条件分岐のためのflag
#    pattern = r'(0?[1-9]|1[0-2])[/\-月](0?[1-9]|[12][0-9]|3[01])日?$'#日付一致の正規表現
    profile = line_bot_api.get_profile(event.source.user_id)
    User_id=profile.user_id
    this_year=2020
    context = "{}"
    context = context.format("plan text,yyyy int,MM int,dd int,hh int,mmmm int,send_id text,issue_id int")
    cur.execute("create table if not exists User"+str(User_id)+"("+context+");")
    cur.execute("SELECT * FROM User"+str(User_id)+";")
    db_data= cur.fetchall()
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
                    TextSendMessage(text="予約を行います日付を教えてください\nex)明日、今日、明後日、11/6\n※予約時刻は10分単位で行います1分単位で予約すると10分繰り上げ通知となります"),               
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
                    r_message=event.message.text           
                    try:
                        k=0
                        r_message=r_message.split("/")
                        for i in r_message:
                            r_message[k]=int(i)
                            k+=1
                        if r_message[0] in list30:
                            if r_message[1]>30:
                                error_flag=1
                        elif r_message[0] in list31:
                            if r_message[1]>31:
                                error_flag=1
                        else:
                            if r_message[1]>28:
                                error_flag=1
                    except:
                        error_flag=1


                    if error_flag == 0:    
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="何時何分に設定しますか\n入力フォーマット例(11時10分のとき):11:10（半角）"),
                        )
                        ws_w.cell(row=b_row,column=flag,value=2)
                        ws_w.cell(row=b_row,column=b_month,value=r_message[0])#issue id
                        ws_w.cell(row=b_row,column=b_day,value=r_message[1])
                    else:
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text="入力ミスがあります。ex)明日、今日、明後日、11/6"),
                        )
                        ws_w.cell(row=b_row,column=flag,value=1)
        #               ws_w.cell(row=b_row,column=buffer1,value=event.message.text)
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
                    ws_w.cell(row=b_row,column=b_hour,value=r_message[0])#issue id
                    ws_w.cell(row=b_row,column=b_minute,value=r_message[1])#issue id
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

#                k=0
#                for i in range(2,201):
#                    issue_id=i
#                    k=i
#                    if type(ws.cell(row=issue_id,column=issue_id_col).value) == type(1):
#                        continue
#                    else:
#                        ws_w.cell(row=issue_id,column=issue_id_col,value=issue_id)
#                        break


                issue_id=10000

                #予定の処理
                ws_w.cell(row=issue_id,column=buffer3,value=ws.cell(row=b_row,column=buffer3).value)
                #普通に日付を入れたときの処理
                ws_w.cell(row=issue_id,column=yyyy,value=this_year)
                ws_w.cell(row=issue_id,column=MM,value=ws.cell(row=b_row,column=b_month).value)
                ws_w.cell(row=issue_id,column=dd,value=ws.cell(row=b_row,column=b_day).value)
                ws_w.cell(row=issue_id,column=hh,value=ws.cell(row=b_row,column=b_hour).value)
                ws_w.cell(row=issue_id,column=mm,value=ws.cell(row=b_row,column=b_minute).value)
                month=datetime.now().month
                day=datetime.now().day
                #今日明日明後日の処理
                #print(str(ws.cell(row=2,column=buffer1).value) == "今日")
                if ws.cell(row=b_row,column=buffer1).value=="今日":
                    ws_w.cell(row=issue_id,column=MM,value=month)
                    ws_w.cell(row=issue_id,column=dd,value=day)

                #tomorrow
                elif ws.cell(row=b_row,column=buffer1).value == "明日":
                    ws_w.cell(row=issue_id,column=MM,value=month)#month
                    tomorrow=day+1
                    ws_w.cell(row=issue_id,column=dd,value=tomorrow)
                    #save and reopen
                    wb_w.save("user"+str(User_id)+".xlsx")
                    wb=px.load_workbook("user"+str(User_id)+".xlsx")#reopen xls file(wb=work book)
                    ws = wb["plan"]#get sheet data(ws=work sheet)

                    #月繰り上げ処理:list30は30日まで、list31は31日まで
                    if int(ws.cell(row=issue_id,column=MM).value) in list30:
                        if tomorrow>30:
                            ws_w.cell(row=issue_id,column=dd,value=tomorrow-30)
                            Month=ws.cell(row=issue_id,column=MM).value
                            ws_w.cell(row=issue_id,column=MM,value=Month+1)
                    
                    elif int(ws.cell(row=issue_id,column=MM).value) in list31:
                        if tomorrow>31:
                            ws_w.cell(row=issue_id,column=dd,value=tomorrow-31)
                            Month=ws.cell(row=issue_id,column=MM).value
                            ws_w.cell(row=issue_id,column=MM,value=Month+1)
                    #2月の処理
                    else:
                        if tomorrow>28:
                            ws_w.cell(row=issue_id,column=dd,value=day-28)
                            Month=ws.cell(row=issue_id,column=MM).value
                            ws_w.cell(row=issue_id,column=MM,value=Month+1)



                #day after tomorrow
                elif ws.cell(row=b_row,column=buffer1).value == "明後日":
                    ws_w.cell(row=issue_id,column=MM,value=month)#month
                    d_a_tomorrow=day+2
                    ws_w.cell(row=issue_id,column=dd,value=d_a_tomorrow)
                    #save and reopen
                    wb_w.save("user"+str(User_id)+".xlsx")
                    wb=px.load_workbook("user"+str(User_id)+".xlsx")#reopen xls file(wb=work book)
                    ws = wb["plan"]#get sheet data(ws=work sheet)

                    #月繰り上げ処理
                    if int(ws.cell(row=issue_id,column=MM).value) in list30:
                        if d_a_tomorrow>29:
                            ws_w.cell(row=issue_id,column=dd,value=d_a_tomorrow-30)
                            Month=ws.cell(row=issue_id,column=MM).value
                            ws_w.cell(row=issue_id,column=MM,value=Month+1)
                    
                    elif int(ws.cell(row=issue_id,column=MM).value) in list31:
                        if d_a_tomorrow>30:
                            ws_w.cell(row=issue_id,column=dd,value=d_a_tomorrow-31)
                            Month=ws.cell(row=issue_id,column=MM).value
                            ws_w.cell(row=issue_id,column=MM,value=Month+1)
                    #2月の処理
                    else:
                        if d_a_tomorrow>27:
                            ws_w.cell(row=issue_id,column=dd,value=d_a_tomorrow-28)
                            Month=ws.cell(row=issue_id,column=MM).value
                            ws_w.cell(row=issue_id,column=MM,value=Month+1)


                wb_w.save("user"+str(User_id)+".xlsx")
                wb=px.load_workbook("user"+str(User_id)+".xlsx")#reopen xls file(wb=work book)
                ws = wb["plan"]#get sheet data(ws=work sheet)
                
                #年明け処理
                if int(ws.cell(row=issue_id,column=MM).value) >12:
                    ws_w.cell(row=issue_id,column=MM,value=1)
                    ws_w.cell(row=issue_id,column=yyyy,value=this_year+1)

                wb_w.save("user"+str(User_id)+".xlsx")
                wb=px.load_workbook("user"+str(User_id)+".xlsx")#open xls file(wb=work book)
                ws = wb["plan"]#get sheet data(ws=work sheet)

                #翌年への移行もし明日の処理とかできたらましたのif文はいらない



                if datetime.now() > datetime(year=this_year,month=ws.cell(row=issue_id,column=MM).value,day=ws.cell(row=issue_id,column=dd).value,hour=ws.cell(row=issue_id,column=hh).value,minute=ws.cell(row=issue_id,column=mm).value):
                    ws_w.cell(row=issue_id,column=yyyy,value=this_year+1)
                else:
                    ws_w.cell(row=issue_id,column=yyyy,value=this_year)



                wb_w.save("user"+str(User_id)+".xlsx")
                wb=px.load_workbook("user"+str(User_id)+".xlsx")#open xls file(wb=work book)
                ws = wb["plan"]#get sheet data(ws=work sheet)

                Plan=ws.cell(row=issue_id,column=plan).value
                Year=int(ws.cell(row=issue_id,column=yyyy).value)
                Month=int(ws.cell(row=issue_id,column=MM).value)
                Day=int(ws.cell(row=issue_id,column=dd).value)
                Hour=int(ws.cell(row=issue_id,column=hh).value)
                Minute=int(ws.cell(row=issue_id,column=mm).value)
                Send_id=str(ws.cell(row=issue_id,column=send_id).value)
                Issue_id=str(ws.cell(row=issue_id,column=issue_id_col).value)

                cur.execute("insert into User"+str(User_id)+"demo values(%s,%s,%s,%s,%s,%s,%s,%s);",(Plan,Year,Month,Day,Hour,Minute,Send_id,Issue_id))
                if issue_id == 200:
                    line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text="予約上限です\n削除するか通知を待ってから追加できます"),        
                    )
                    
                else:
                    if type(ws.cell(row=b_row,column=buffer1).value) == type("hello"):#buffer1の内容はb_rowからissue_idに移していない
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=str(ws.cell(row=b_row,column=buffer1).value)+"の"+str(ws.cell(row=issue_id,column=hh).value)+"時"+str(ws.cell(row=issue_id,column=mm).value)+"分に"+"”"+str(ws.cell(row=b_row,column=buffer3).value)+"”"+"で予約しました。\n"+str(issue_id)),        
                        )
                    else:
                        line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=str(ws.cell(row=issue_id,column=yyyy).value)+"年"+str(ws.cell(row=issue_id,column=MM).value)+"月"+str(ws.cell(row=issue_id,column=dd).value)+"日の"+str(ws.cell(row=issue_id,column=hh).value)+"時"+str(ws.cell(row=issue_id,column=mm).value)+"分に"+"”"+str(ws.cell(row=b_row,column=buffer3).value)+"”"+"で予約しました。\n"+str(issue_id)),        
                        )



#                    if ws.cell(row=b_row,column=b_month).value != 0:
#                        line_bot_api.reply_message(
#                        event.reply_token,
#                        TextSendMessage(text=str(ws.cell(row=issue_id,column=yyyy).value)+"年"+str(ws.cell(row=issue_id,column=MM).value)+"月"+str(ws.cell(row=issue_id,column=dd).value)+"日の"+str(ws.cell(row=issue_id,column=hh).value)+"時"+str(ws.cell(row=issue_id,column=mm).value)+"分に"+"”"+str(ws.cell(row=b_row,column=buffer3).value)+"”"+"で予約しました。\n"+str(issue_id)),        
#                        )
#                    else:
#                        line_bot_api.reply_message(
#                        event.reply_token,
#                        TextSendMessage(text=str(ws.cell(row=b_row,column=buffer1).value)+"の"+str(ws.cell(row=b_row,column=b_hour).value)+"時"+str(ws.cell(row=b_row,column=b_minute).value)+"分に"+"”"+str(ws.cell(row=b_row,column=buffer3).value)+"”"+"で予約しました。\n"+str(issue_id)),        
#                        )





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