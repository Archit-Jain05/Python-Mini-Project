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
    return flag
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
       return flag
def newuser(username,password,age,country,opt):
    age=str(age)
    sql="INSERT INTO users VALUES(\""+username+"\",\""+password+"\","+age+",\""+country+"\","+opt[0]+","+opt[1]+","+opt[2]+","+opt[3]+","+opt[4]+","+opt[5]+","+opt[6]+");"
    print(sql)
    cur.execute(sql)
    print("Succesfull entry")
    conn.commit()
def updateuser(username,password,age,country,opt):
    age=str(age)
    sql="UPDATE `users` SET `pass`='"+password+"',`age`="+age+",`country`='"+country+"',`politics`='"+opt[0]+"',`sports`='"+opt[1]+"',`entertainment`='"+opt[2]+"',`weather`='"+opt[3]+"',`crime`='"+opt[4]+"',`science and technology`='"+opt[5]+"',`wildlife`='"+opt[6]+"' WHERE username='"+username+"';"
    print(sql)
    cur.execute(sql)
    conn.commit()
    print("User updated")

opt=[1,1,1,1,1,1,1]
opt=list(map(lambda x: str(x),opt))
opt2=[0,0,0,0,0,0,0]
opt2=list(map(lambda x: str(x),opt2))
#newuser("Archit","123",19,"India",opt)
#getall()
updateuser("Archit","123",19,"India",opt2)