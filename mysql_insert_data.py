import mysql.connector
con_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()
# query="insert into human values(%s,%s,%s,%s)"   #  %s is placeholder for data
# values=(2,"dwd",24,"hyd")
# cur_obj.execute(query,values)
# con_obj.commit()    #without commit method data won't be inserted

cur_obj.execute("insert into human values(5,'bcc',44,'bkk')")
con_obj.commit()

#  select *from human;
# +----+--------+------+---------+
# | id | name   | age  | address |
# +----+--------+------+---------+
# |  1 | charan |   22 | hyd     |
# |  2 | dwd    |   24 | hyd     |
# |  3 | dwd    |   24 | hyd     |
# |  5 | bcc    |   44 | bkk     |
# +----+--------+------+---------+
# 4 rows in set (0.00 sec)

print(cur_obj.rowcount," records inserted")     #1  records inserted

#  select *from human;
# +----+--------+------+---------+
# | id | name   | age  | address |
# +----+--------+------+---------+
# |  1 | charan |   22 | hyd     |
# |  2 | dwd    |   24 | hyd     |
# +----+--------+------+---------+
# 2 rows in set (0.00 sec)