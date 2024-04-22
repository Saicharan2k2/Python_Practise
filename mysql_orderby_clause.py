import mysql.connector as m;
con_obj=m.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()
# sql="select *from human order by name"
# cur_obj.execute(sql)
# res =cur_obj.fetchall()
# for x in res:
#     print(x)                                #(5, 'bcc', 44, 'bkk')
                                            # (4, 'ccc', 54, 'kcjc')
                                            # (6, 'ccti', 77, 'jnon')
                                            # (7, 'ceiucu', 49, 'ncnc')
                                            # (1, 'charan', 22, 'hyd')
                                            # (3, 'dwd', 24, 'hyd')
                                            # (2, 'dwd', 24, 'hyd')
                                            # (10, 'jfnf', 33, 'bc cnc')
                                            # (8, 'oirugor', 89, 'jhcui')
                                            # (11, 'uuuhk', 37, 'ojoj')

sql="select *from human order by name desc"
cur_obj.execute(sql)
res=cur_obj.fetchall()
for x in res:
    print(x)                                #(11, 'uuuhk', 37, 'ojoj')
                                            # (8, 'oirugor', 89, 'jhcui')
                                            # (10, 'jfnf', 33, 'bc cnc')
                                            # (2, 'dwd', 24, 'hyd')
                                            # (3, 'dwd', 24, 'hyd')
                                            # (1, 'charan', 22, 'hyd')
                                            # (7, 'ceiucu', 49, 'ncnc')
                                            # (6, 'ccti', 77, 'jnon')
                                            # (4, 'ccc', 54, 'kcjc')
                                            # (5, 'bcc', 44, 'bkk')