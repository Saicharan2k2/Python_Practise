import mysql.connector
con_obj=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="charan"
)
my_cursor=con_obj.cursor()
my_cursor.execute("Show databases")
for x in my_cursor:
    print(x)
    print(type(x))

# ('information_schema',)
# <class 'tuple'>
# ('charan',)
# <class 'tuple'>
# ('mysql',)
# <class 'tuple'>
# ('performance_schema',)
# <class 'tuple'>
# ('sai',)
# <class 'tuple'>
# ('test',)
# <class 'tuple'>

my_cursor.execute("Show tables")
for x in my_cursor:
    print(x)
    print(type(x))

# ('human',)
# <class 'tuple'>