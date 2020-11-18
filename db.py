import psycopg2 as p2
import psycopg2.extras



connection = p2.connect("host=ec2-3-213-106-122.compute-1.amazonaws.com port=5432 dbname=dap1bs8ml5o18m user=lenlmwyicflwcu password=a6d1cfd820fd5146b52ebf39c8a6bde0d5e71e1ec5b12fd85307ecb43ccf928d")
dictcur = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
#自動トランザクション
connection.autocommit = True
print(connection.get_backend_pid())


#これによってSQLオブジェクトを使用可能にする
cur = connection.cursor()
#print(cur)
cur.execute("create table demo(id int,data text,day date)")
cur.execute("insert into demo values(1,'HELLOWORLDMYNAMEISKAITO','2020/11/18');")
cur.execute("insert into demo values(2,'HELLO MMA','2020/11/19');")


#saveみたいな意味
connection.commit()
"""
dictcur.execute('SELECT * FROM demo;')
results = dictcur.fetchall()
for r in results:
  print(r['column'])
"""

#SQL文の実行
cur.execute("SELECT * FROM demo;")
results= cur.fetchall()
for i in results:
    print(i[0],i[1],type(i[2]))

#DBの削除
cur.execute("drop table demo;")


#cur.execute("select id, data from demo")
#for row in cur:
#    print(row[0],row[1])