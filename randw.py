import openpyxl as px
import pprint
from random import randint
import re
from datetime import date,datetime,timedelta

from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
import os

#today's infomation
year=datetime.now().year
month=datetime.now().month
today=datetime.now().day
hour=datetime.now().hour
minute=datetime.now().minute


your_file_list=["./sample.xlsx","./sample2.xlsx"]

list30=[4,6,9,11]
list31=[1,3,5,7,8,10,12]
#Max_issue_id
max_issue_id=100

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
buffer_id=17
buffer_date=18
true_date=19
true_time=20


for your_file in your_file_list: 

    wb=px.load_workbook(your_file)#open xls file(wb=work book)
    ws = wb["plan"]#get sheet data(ws=work sheet)

    LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]

    line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
    user_id = ws.cell(row=1,column=1).value

    wb_w=px.load_workbook(your_file)
    ws_w=wb_w.worksheets[0]
    ws_w.cell(row=8,column=2,value="")
    wb_w.save(your_file)
    wb=px.load_workbook(your_file)#open xls file(wb=work book)
    ws = wb["plan"]

    for i in range(2,201):
        is_issueid = ws.cell(row=i,column=issue_id_col).value
        if is_issueid != None:
            if datetime(ws.cell(row=i,column=yyyy).value,ws.cell(row=i,column=MM).value,ws.cell(row=i,column=dd).value,ws.cell(row=i,column=hh).value,ws.cell(row=i,column=mm).value) < datetime.now():
                message = TextSendMessage(text=str(ws.cell(row=i,column=buffer3).value)+"の時間です！"+str(ws.cell(row=8,column=2).value))
                line_bot_api.push_message(user_id,message)
                ws_w.cell(row=i,column=issue_id_col,value="")
                wb_w.save(your_file)
                #issue_idの削除

