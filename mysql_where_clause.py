import mysql.connector as m
con_obj=m.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()
# cur_obj.execute("select *from human where address='hyd'")
# res=cur_obj.fetchall()
# for x in res:                   #(1, 'charan', 22, 'hyd')
#                                 # (2, 'dwd', 24, 'hyd')
#                                 # (3, 'dwd', 24, 'hyd')
#     print(x)

# wildcard characters
# cur_obj.execute("select *from human where address like '%cn%'")
# res=cur_obj.fetchall()
# for x in res:
#     print(x)                    #(7, 'ceiucu', 49, 'ncnc')
                                #(10, 'jfnf', 33, 'bc cnc')

sql="select *from human where address like %s"
adr=('jnon',)
cur_obj.execute(sql,adr)
res=cur_obj.fetchall()
for x in res:
    print(x)                    #(6, 'ccti', 77, 'jnon')