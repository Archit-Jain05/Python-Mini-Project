import mysql.connector

try:
   conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="vianewscredentials"
)
except(mysql.connector.errors.InterfaceError):
   print("Cannot establish connection")
   exit()

if conn:
   print("Database Connection Established Successfully")
   pass
else:
   print("Database Connection Error")


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
    return flag


def validatepass(password):
    flag=0
    sql = "SELECT * FROM users WHERE pass LIKE \""+password+"\";"
    cur.execute(sql)
    for row in cur:
       flag=1
       return flag
    

def validatelogin(usn,password):
   f1=validateuser(usn)
   flag=0
   if f1==1:  
      sql = "SELECT * FROM users WHERE pass LIKE \""+password+"\" and username LIKE \""+usn+"\";"
      cur.execute(sql)
      for row in cur:
         flag=1
      if flag!=1:
         flag=0
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

conn.commit()