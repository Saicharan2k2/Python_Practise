#establishing connection with MySQL database
#import mysql driver connector
import mysql.connector
#collect mysql object reference ,call connect method 
con_object=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
print(con_object)   #<mysql.connector.connection.MySQLConnection object at 0x000001F4BDC89B20>
#collect cursor object to point to data in database
my_cursor=con_object.cursor()
#my_cursor.execute("create database charan")  #mysql> show databases;
# +--------------------+
# | Database           |
# +--------------------+
# | information_schema |
# | charan             |
# | mysql              |
# | performance_schema |
# | sai                |
# | test               |
# +--------------------+
# 6 rows in set (0.10 sec)
try:
  my_cursor.execute("create table human(id int primary key,name varchar(11),age int,address varchar(11))")
#    use charan;
# Database changed
# mysql> show tables;
# +------------------+
# | Tables_in_charan |
# +------------------+
# | human            |
# +------------------+
# 1 row in set (0.00 sec)

# mysql> desc human;
# +---------+-------------+------+-----+---------+-------+
# | Field   | Type        | Null | Key | Default | Extra |
# +---------+-------------+------+-----+---------+-------+
# | id      | int(11)     | NO   | PRI | NULL    |       |
# | name    | varchar(11) | YES  |     | NULL    |       |
# | age     | int(11)     | YES  |     | NULL    |       |
# | address | varchar(11) | YES  |     | NULL    |       |
# +---------+-------------+------+-----+---------+-------+
# 4 rows in set (0.07 sec)
  print("database connection success and table created successfully")
except:
  print("database connection failed table not created..")