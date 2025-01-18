import mysql.connector as conn

mydb = conn.connect(
    host="localhost",
    user="root",
    password="cvr123",
    database="sridhar"
)

mycursor = mydb.cursor()

id = input("Enter the student ID to update: ")
new_name = input("Enter the new name: ")

update_query = "UPDATE std SET name = %s WHERE id = %s"
mycursor.execute(update_query, (new_name, id))

mydb.commit()

print(f"Student with ID {id} has been updated with the new name: {new_name}")

mycursor.close()
mydb.close()
