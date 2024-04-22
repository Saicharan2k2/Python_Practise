import mysql.connector as m
con_obj=m.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cur_obj=con_obj.cursor()
# sql="select human.name human_name,demo.fav demo_fav from human inner join demo on human.id=demo.id"
sql="SELECT \
  human.name AS user, \
  demo.fav AS favorite \
  FROM human \
  INNER JOIN demo ON human.id = demo.id"
cur_obj.execute(sql)
res=cur_obj.fetchall()
for c in res:                           #('charan', 'lwdjw')
                                        # ('dwd', 'khduehd')
                                        # ('abcd', 'ihdkd')
                                        # ('ccc', 'eudued')
    print(c)