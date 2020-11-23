import psycopg2 as p2
import psycopg2.extras

from datetime import datetime
from datetime import timedelta
from flask import Flask, request, abort

import os

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import  InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage,TemplateSendMessage,ButtonsTemplate,MessageAction


#環境変数取得
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

Host=os.environ.get('PG_HOST')
Port=os.environ.get('PG_PORT')
Database=os.environ.get('PG_DBNM')
User=os.environ.get('PG_USER')
Password=os.environ.get('PG_PASS')
user_id=os.environ.get('USER_ID')
connection = p2.connect("host="+str(Host)+" port="+str(Port)+" dbname="+str(Database)+" user="+str(User)+" password="+str(Password))
#自動トランザクション
connection.autocommit = True
#print(connection.get_backend_pid())
#context = "{}"
#context = context.format("id int,data text,day date,min time")
#これによってSQLオブジェクトを使用可能にする
cur = connection.cursor()
#print(cur)
#val=1
#char=send_id
#day='2020/11/20'
#tim='11:11'
#cur.execute("create table if not exists "+str("hello")+"demo("+context+");")
#print(cur.execute("select count (*) from hellodemo;"))
#cur.execute("insert into hellodemo values(NULL,'HELLO MMA','2020/11/19','11:11');")
#py変数の代入
#cur.execute("insert into "+str("hello")+"demo values(%s,%s,%s,%s);",(val,char,day,tim))
#cur.execute("delete from hellodemo where id =1")
#cur.execute("delete from hellodemo where id =2")

#saveみたいな意味
connection.commit()

#SQL文の実行
#cur.execute("SELECT * FROM "+str(send_id)+";")
#results= cur.fetchall()
dictcur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

#DB内テーブル取得
cur.execute("select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';")
each_table=cur.fetchall()
for i in each_table:
  send_id=str(i[0])
  dictcur.execute("SELECT * FROM "+send_id+";")
  result_dict=dictcur.fetchall()
  dict_result = []
  #ここのループで辞書にしている
  for row in result_dict:
      dict_result.append(dict(row))
  len_dic=len(result_dict)

  for row in range(len_dic):
    plan=dict_result[row]["plan"]
    year=dict_result[row]["yyyy"]  
    month=dict_result[row]["mm"]
    day=dict_result[row]["dd"]
    hour=dict_result[row]["hh"]
    minute=dict_result[row]["mmmm"]
    issue_id=dict_result[row]["issue_id"]
    #日本時間に合わせる作業
    nowon=datetime.now()
    nowon+=timedelta(hours=9)
    plan_date=datetime(year=year,month=month,day=day,hour=hour,minute=minute)

    if nowon >= plan_date:
      line_bot_api.push_message(send_id, TextSendMessage(text=str(plan)+"の時間です。"))
      dictcur.execute("delete from "+send_id+" where issue_id="+str(issue_id))


#print(len_dic)
#print(dict_result[len_dic-1]["data"])

#DBの削除
#cur.execute("drop table if exists hellodemo;")


#cur.execute("select id, data from demo")
#for row in cur:
#    print(row[0],row[1])

#cur.execute("select * from "+str(user_id))
#cur.execute("delete from user"+str(user_id)+" where issue_id=10000")

