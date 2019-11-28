import pymysql

#连接数据库
db = pymysql.connect("localhost", "root", "123", "mytest")
cursor = db.cursor()

#执行sql
sql = "select * from t_user"
cursor.execute(sql)

result = cursor.fetchall()

#打印结果
for row in result:
    id = row[0]
    username = row[1]
    password = row[2]
    age = row[3]

    print("""id = %s , username = %s ,password = %s ,age = %s""" % (id, username, password, age))

