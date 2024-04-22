import mysql.connector as m
con_obj=m.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()
# sql="drop table demo"
sql="drop table if exists demo"
cur_obj.execute(sql)
che="show tables like 'demo'"
cur_obj.execute(che)
res=cur_obj.fetchone()
if res is None:
    print("table is deleted..")                         #table is deleted..
else:                                                   #show tables;
                                                        # +------------------+
                                                        # | Tables_in_charan |
                                                        # +------------------+
                                                        # | human            |
                                                        # +------------------+
                                                        # 1 row in set (0.00 sec)
    print("table still exists..")
cur_obj.close()
con_obj.close()
