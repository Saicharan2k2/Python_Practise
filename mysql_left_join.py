import mysql.connector as m
con_obj=m.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()
#              -------LEFT JOIN-------
sql="select human.name hname,demo.fav fav from human left join demo on human.id=demo.id"
cur_obj.execute(sql)
res=cur_obj.fetchall()
for x in res:
    print(x)
print(cur_obj.rowcount,"rows ")             #('charan', 'lwdjw')
                                    # ('dwd', 'khduehd')
                                    # ('abcd', 'ihdkd')
                                    # ('ccc', 'eudued')
                                    # ('bcc', None)
                                    # ('ccti', None)
                                    # ('ceiucu', None)
                                    # ('oirugor', None)
                                    # 8 rows

#       ------RIGHT JOIN------
sql2="select human.name hname,demo.fav fav from human right join demo on human.id=demo.id"
cur_obj.execute(sql2)
res2 =cur_obj.fetchall()
for y in res2:
    print(y)
print(cur_obj.rowcount," rows ")
                                    # ('charan', 'lwdjw')
                                    # ('dwd', 'khduehd')
                                    # ('abcd', 'ihdkd')
                                    # ('ccc', 'eudued')
                                    # 4  rows