# 使用Python操作数据库

import math
import pymysql

# 数据库基础信息
DATABASE = {
    'host': "127.0.0.1",
    'port': 3306,
    'user': "root",
    'password': "123321",
    'db': "test",  # 要使用的数据库名字 默认为空
    'charset': "utf8mb4",
    # 'cursorclass': pymysql.cursors.DictCursor
}

# 连接MySql数据库
connection = pymysql.connect(**DATABASE, cursorclass=pymysql.cursors.DictCursor)

# 通过cursors创建游标
cursor = connection.cursor()

# 执行语句
sql = "select * from person"

cursor.execute(sql)

result = cursor.fetchall()

for row in result:
    print(row)

print(" 花蕾的分割线 =========== ")

sql2 = "select name,fav ,work from person"

cursor.execute(sql2)

for row in cursor.fetchall():
    print(row)
    

# fetchone() 用于查询单条数据。
# fetchall() 用于查询多条数据。
# close() 最后不要忘记了关闭数据连接。
# 关闭连接
connection.close()
