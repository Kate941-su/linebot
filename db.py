import psycopg2 as p2
import psycopg2.extras
import os


Host=os.environ.get('PG_HOST')
Port=os.environ.get('PG_PORT')
Database=os.environ.get('PG_DBNM')
User=os.environ.get('PG_USER')
Password=os.environ.get('PG_PASS')
user_id=os.environ.get('USER_ID')
connection = p2.connect("host="+str(Host)+" port="+str(Port)+" dbname="+str(Database)+" user="+str(User)+" password="+str(Password))



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
#cur.execute("insert into hellodemo values(NULL,'HELLO MMA','2020/11/19','11:11');")
#py変数の代入
cur.execute("insert into "+str("hello")+"demo values(%s,%s,%s,%s);",(val,char,day,tim))
#cur.execute("delete from hellodemo where id =1")
#cur.execute("delete from hellodemo where id =2")


#saveみたいな意味
connection.commit()

#SQL文の実行
cur.execute("SELECT * FROM hellodemo;")
results= cur.fetchall()
#print(results)

#print(len(results))
#for record in results:
#  if record[0] == None:
#    print("hello")


dictcur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
dictcur.execute("SELECT * FROM hellodemo;")
result_dict=dictcur.fetchall()
dict_result = []
#ここのループで辞書にしている
for row in result_dict:
    dict_result.append(dict(row))
print(dict_result)
len_dic=len(result_dict)
#print(len_dic)
#print(dict_result[len_dic-1]["data"])

#DBの削除
#cur.execute("drop table if exists hellodemo;")


#cur.execute("select id, data from demo")
#for row in cur:
#    print(row[0],row[1])

#cur.execute("select * from "+str(user_id))
#cur.execute("delete from user"+str(user_id)+" where issue_id=10000")

