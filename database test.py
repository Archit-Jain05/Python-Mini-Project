import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="vianewscredentials"
)
if conn:
  print("Connection Established Successfully")
else:
  print("Connection Error")

cur=conn.cursor()
cur.execute("SELECT * FROM users")
for row in cur:
    print(row)