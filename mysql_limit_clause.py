import mysql.connector as m
con_obj=m.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()
# sql="select *from human limit 5"
# cur_obj.execute(sql)
# res =cur_obj.fetchall()
# for x in res:
#     print(x)                    #(1, 'charan', 22, 'hyd')
                                # (2, 'dwd', 69, 'hyd')
                                # (3, 'abcd', 24, 'hyd')
                                # (4, 'ccc', 54, 'kcjc')
                                # (5, 'bcc', 44, 'bkk')

# starting from some row using offset clause
sql="select *from human limit 4 offset 2"
cur_obj.execute(sql)
res=cur_obj.fetchall()
for x in res:
    print(x)                        #(3, 'abcd', 24, 'hyd')
                                    # (4, 'ccc', 54, 'kcjc')
                                    # (5, 'bcc', 44, 'bkk')
                                    # (6, 'ccti', 77, 'jnon')