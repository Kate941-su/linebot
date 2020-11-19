import psycopg2 as p2
import psycopg2.extras



connection = p2.connect("host=ec2-3-213-106-122.compute-1.amazonaws.com port=5432 dbname=dap1bs8ml5o18m user=lenlmwyicflwcu password=a6d1cfd820fd5146b52ebf39c8a6bde0d5e71e1ec5b12fd85307ecb43ccf928d")
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
print(cur.execute("select count (*) from hellodemo;"))
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