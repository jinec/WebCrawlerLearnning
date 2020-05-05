import pymysql
#connect(数据库地址，用户名，密码，数据库名)
#连接mysql服务器
db=pymysql.connect("localhost",'root','bbbbbb',"zhilian")
#创建游标对象
cursor=db.cursor()
#执行sql语句
# sql="show tables"
sql="insert into user(id,name) values(7,'zhangsan1')"
# sql="delete from user"
cursor.execute(sql)
db.commit() #提交
#得到返回的结果
# print(cursor.fetchone()) #注意这一句会改变游标的位置
# print(cursor.fetchall())
#查看影响的条数 rowcount，借此查看此步操作是否成功了
print(cursor.rowcount)
#关闭数据库
db.close()