import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="myfirstdatabase"
)

# mycursor.execute("DROP TABLE customers")   this command comes after instance have been generated 
# to delete or drop the table we can also use the same format
# after connection has been made to delete the database itself

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE RegisterAccount(id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(80) NOT NULL, lastname VARCHAR(80) NOT NULL, email VARCHAR(100) NOT NULL, username VARCHAR(50) NOT NULL, password VARCHAR(255) NOT NULL )")


