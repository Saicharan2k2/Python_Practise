import mysql.connector
con_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()                                  #(1, 'charan', 22, 'hyd')
#                                                         (2, 'dwd', 24, 'hyd')
#                                                         (3, 'dwd', 24, 'hyd')
#                                                         (4, 'ccc', 54, 'kcjc')
#                                                         (5, 'bcc', 44, 'bkk')
#                                                         (6, 'ccti', 77, 'jnon')
#                                                         (7, 'ceiucu', 49, 'ncnc')
#                                                         (8, 'oirugor', 89, 'jhcui')
#                                                         (10, 'jfnf', 33, 'bc cnc')
#                                                         (11, 'uuuhk', 37, 'ojoj')
# cur_obj.execute("select *from human")
# result=cur_obj.fetchall()                                 #all rows 
# for c in result:
#     print(c)
# cur_obj.execute("select id,name from human")
# result=cur_obj.fetchall()                               #(1, 'charan')
                                                        # (2, 'dwd')
                                                        # (3, 'dwd')
                                                        # (4, 'ccc')
                                                        # (5, 'bcc')
                                                        # (6, 'ccti')
                                                        # (7, 'ceiucu')
                                                        # (8, 'oirugor')
                                                        # (10, 'jfnf')
                                                        # (11, 'uuuhk')
# for x in result:                                      # selecting specific columns
#     print(x)

cur_obj.execute("select *from human")
res=cur_obj.fetchone()                                  #selecting one row(first)
print(res)                                              #(1, 'charan', 22, 'hyd')