import mysql.connector

con_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
cursor_obj=con_obj.cursor()
# cursor_obj.execute("alter table human drop primary key")
cursor_obj.execute("alter table human add primary key(id)")