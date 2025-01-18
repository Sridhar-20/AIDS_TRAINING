import mysql.connector as conn

mydb = conn.connect(
    host="localhost",
    user="root",
    password="cvr123",
    database="sridhar"
)

mycursor = mydb.cursor()

id = input("Enter the student ID to delete: ")

delete_query = "DELETE FROM std WHERE id = %s"
mycursor.execute(delete_query, (id,))

mydb.commit()

print(f"Student with ID {id} has been deleted.")

mycursor.close()
mydb.close()
