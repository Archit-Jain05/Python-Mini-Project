import mysql.connector

conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="vianewscredentials"
)
if conn:
  #print("Connection Established Successfully")
  pass
else:
  print("Connection Error")

cur=conn.cursor()

def getall():
    cur.execute("SELECT * FROM users")
    for row in cur:
        print(row)
        

def printres(cur):
   for row in cur:
      print(row)

def validate(usn):
    flag=0
    sql = "SELECT * FROM users WHERE username LIKE \""+usn+"\""
    cur.execute(sql)
    for row in cur:
       flag=1
    if flag==1:
       print("Valid")
    else:
       print("Invalid")

#validate("Vanshita")

def newuser(username,password,age,country,opt1,opt2,opt3,opt4,opt5,opt6,op7):
   age=str(age)
   opt1
   sql="insert into users VALUES(\""+username+"\",\""+password+"\","+age+",\""+country+"\")"
   print(sql)

newuser("Iqra","123",19,"India")