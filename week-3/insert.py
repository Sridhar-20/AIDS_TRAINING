import mysql.connector as conn
mydb=conn.connect(
    host="localhost",
    user="root",
    password="cvr123",
    database="sridhar"
)
mycursor=mydb.cursor()

id=input("Enter your id")
name=input("enter the name")
marks=input("enter the marks")
city=input("enter the city")
mycursor.execute("INSERT INTO std (id, name, marks, city) values(%s,%s,%s,%s)",(id,name,marks,city))

mydb.commit()
