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
def validateuser(usn):
    flag=0
    sql = "SELECT * FROM users WHERE username LIKE \""+usn+"\""
    cur.execute(sql)
    for row in cur:
       flag=1
    if flag==1:
       print("Valid")
    else:
       print("Invalid")
def validatepass(password):
    flag=0
    sql = "SELECT * FROM users WHERE username LIKE \""+password+"\""
    cur.execute(sql)
    for row in cur:
       flag=1
    if flag==1:
       print("Valid Password")
    else:
       print("Invalid Password")
def newuser(username,password,age,country,opt):
    age=str(age)
    sql="INSERT INTO users VALUES(\""+username+"\",\""+password+"\","+age+",\""+country+"\","+opt[0]+","+opt[1]+","+opt[2]+","+opt[3]+","+opt[4]+","+opt[5]+","+opt[6]+");"
    print(sql)
    cur.execute(sql)
    print("Succesfull entry")
    conn.commit()
def updateuser(username,password,age,country,opt):
   age=str(age)



#opt=[1,1,1,1,1,1,1]
#opt=list(map(lambda x: str(x),opt))
#newuser("Iqra","123",19,"India",opt)
#getall()