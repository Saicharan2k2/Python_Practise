import mysql.connector as m
con_obj=m.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()
# sql="delete from human where address='ojoj'"
# cur_obj.execute(sql)
# con_obj.commit()
# print(cur_obj.rowcount," rows deleted..")       #1  rows deleted..
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
                                                    # | 10 | jfnf    |   33 | bc cnc  |
                                                    # +----+---------+------+---------+
                                                    # 9 rows in set (0.00 sec)

# here placeholder %s is used to prevent SQL injection by using direct values in query can lead to data breach
sql="delete from human where address=%s" 
adr=("bc cnc",)
cur_obj.execute(sql,adr)
con_obj.commit()
print(cur_obj.rowcount," rows deleted")             #1  rows deleted
                                                    #select *from human;
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