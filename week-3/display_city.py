
import mysql.connector as c
mydb = c.connect(
  host="localhost",
  user="root",
  password="cvr123",
  database="sridhar"
)
mycursor = mydb.cursor()

mycursor.execute("select * from std where city='hyd'")
std=mycursor.fetchall()
print("Student details whose city is hyd")
for s in std:

    print(f"ID: {s[0]}, Name: {s[1]}, Marks: {s[2]}, City: {s[3]}")
mydb.commit()
