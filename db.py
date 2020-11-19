import psycopg2 as p2
import psycopg2.extras
import os


Host=os.environ.get('PG_HOST')
Port=os.environ.get('PG_PORT')
Database=os.environ.get('PG_DBNM')
User=os.environ.get('PG_USER')
Password=password=os.environ.get('PG_PASS')
connection = p2.connect("host="+str(Host)+" port="+str(Port)+" dbname="+str(Database)+" user="+str(User)+" password="+str(Password))

#connection = p2.connect(
#    host=os.environ.get('PG_HOST'),
#    port=os.environ.get('PG_PORT'),
#    database=os.environ.get('PG_DBNM'),    
#    user=os.environ.get('PC_USER'), 
#    password=os.environ.get('PG_PASS'),
#)

dictcur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
#自動トランザクション
connection.autocommit = True
print(connection.get_backend_pid())

context = "{}"
context = context.format("id int,data text,day date,min time")
#これによってSQLオブジェクトを使用可能にする
cur = connection.cursor()
#print(cur)
val=1
char='hellokitayakaito'
day='2020/11/20'
tim='11:11'
cur.execute("create table if not exists "+str("hello")+"demo("+context+");")
#print(cur.execute("select count (*) from hellodemo;"))
cur.execute("insert into hellodemo values(2,'HELLO MMA','2020/11/19','11:11');")
#py変数の代入
cur.execute("insert into "+str("hello")+"demo values(%s,%s,%s,%s);",(val,char,day,tim))
cur.execute("delete from hellodemo where id =1")
cur.execute("delete from hellodemo where id =2")


#saveみたいな意味
connection.commit()
"""
dictcur.execute('SELECT * FROM hellodemo;')
results = dictcur.fetchall()
for r in results:
  print(r['column'])
"""

#SQL文の実行
cur.execute("SELECT * FROM hellodemo;")
results= cur.fetchall()
print(len(results))
for record in results:
    print(record)

#DBの削除
#cur.execute("drop table if exists hellodemo;")


#cur.execute("select id, data from demo")
#for row in cur:
#    print(row[0],row[1])