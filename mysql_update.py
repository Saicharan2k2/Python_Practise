import mysql.connector as m
con_obj=m.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()
# cur_obj.execute("update human set age = 69 where id = 2")
# con_obj.commit()                #select *from human;
                                # +----+---------+------+---------+
                                # | id | name    | age  | address |
                                # +----+---------+------+---------+
                                # |  1 | charan  |   22 | hyd     |
                                # |  2 | dwd     |**69**| hyd     |
                                # |  3 | dwd     |   24 | hyd     |
                                # |  4 | ccc     |   54 | kcjc    |
                                # |  5 | bcc     |   44 | bkk     |
                                # |  6 | ccti    |   77 | jnon    |
                                # |  7 | ceiucu  |   49 | ncnc    |
                                # |  8 | oirugor |   89 | jhcui   |
                                # +----+---------+------+---------+
                                # 8 rows in set (0.00 sec)

# to prevent SQL injection
sql="update human set name=%s where id=%s"
name=("abcd",3)
cur_obj.execute(sql,name)
con_obj.commit()

                                                # select *from human;
                                                # +----+---------+------+---------+
                                                # | id | name    | age  | address |
                                                # +----+---------+------+---------+
                                                # |  1 | charan  |   22 | hyd     |
                                                # |  2 | dwd     |   69 | hyd     |
                                                # |  3 | abcd    |   24 | hyd     |
                                                # |  4 | ccc     |   54 | kcjc    |
                                                # |  5 | bcc     |   44 | bkk     |
                                                # |  6 | ccti    |   77 | jnon    |
                                                # |  7 | ceiucu  |   49 | ncnc    |
                                                # |  8 | oirugor |   89 | jhcui   |
                                                # +----+---------+------+---------+
                                                # 8 rows in set (0.01 sec)