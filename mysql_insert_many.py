import mysql.connector
con_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()
# query="insert into human values(%s,%s,%s,%s)"
# values=[
#     (4,"ccc",54,"kcjc"),
#     (6,"ccti",77,"jnon"),
#     (7,"ceiucu",49,"ncnc"),
#     (8,"oirugor",89,"jhcui")
# ]
# cur_obj.executemany(query,values)
# con_obj.commit()
# print(cur_obj.rowcount," rows inserted ..")

# select *from human;
# +----+---------+------+---------+
# | id | name    | age  | address |
# +----+---------+------+---------+
# |  1 | charan  |   22 | hyd     |
# |  2 | dwd     |   24 | hyd     |
# |  3 | dwd     |   24 | hyd     |
# |  4 | ccc     |   54 | kcjc    |
# |  5 | bcc     |   44 | bkk     |
# |  6 | ccti    |   77 | jnon    |
# |  7 | ceiucu  |   49 | ncnc    |
# |  8 | oirugor |   89 | jhcui   |
# +----+---------+------+---------+
# 8 rows in set (0.00 sec)


sql="insert into human values(%s,%s,%s,%s)"
values=(11,"uuuhk",37,"ojoj")
cur_obj.execute(sql,values)
con_obj.commit()
print("1 record inserted it's ID is ::",cur_obj.lastrowid)      #1 record inserted it's ID is :: 0