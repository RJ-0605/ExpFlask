
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="jedidiah",
  passwd=""
)

databaselist=[]


mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

  
  (databaselist).append(x)



print(databaselist)

# temporary provisionary fix for checking and creating a specific database 
# there would be ofcourse future modifications 
# but for now just follow the syntax 
if ('myfirstdatabase',) not  in databaselist:
	mycursor.execute("CREATE DATABASE myfirstdatabase")
else:
	'Done'
