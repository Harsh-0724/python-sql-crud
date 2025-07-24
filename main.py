from dotenv import load_dotenv
import mysql.connector
import os
# 1.CREATE

#first connect to mysql database
try:
        
    conn = mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = os,
        database = "python_demo"
    )

    db = conn.cursor()
    print("Connection Established.")
except:
    print("Connection Failed.")


#second create a database
db.execute("CREATE DATABASE IF NOT EXISTS python_demo")
conn.commit()
print("Database Created!")

#create a table in the database

db.execute(
    """
CREATE TABLE IF NOT EXISTS CUSTOMERS(
id INTEGER PRIMARY KEY,
name VARCHAR(50) NOT NULL,
email VARCHAR(50) NOT NULL,
age INTEGER
)
"""
)
conn.commit()
print("Table is created!")

#insert customer values in table

db.execute(
   """
INSERT IGNORE INTO CUSTOMERS VALUES 
(1,'Harsh','harsh@gmail.com',34),
(2,'Anil','Anil@gmail.com',33),
(3,'Jitesh','Jitesh@gmal.com',24),
(4,'Rajat','rajat@gmail.com',22)
"""
)
conn.commit()
print("Rows are inserted")

# 2.READ
db.execute("select * from CUSTOMERS")
result = db.fetchall()
print("Displaying the table:\n")
#for printing entire entry
for x in result:
    print(x)
print("\nDisplaying only names in the table:\n")
#for printing only names
for x in result:
    print(x[1])


# 3.UPDATE

db.execute("update customers set age = 50 where id = 1")
conn.commit()
print("Updated")

db.execute("update customers set email = 'HARSH@GMAIL.COM' where id = 1")
conn.commit()
print("Updated")

# 4.DELETETE

db.execute("delete from customers where id = 4")
conn.commit()
print("Element Deleted")

db.execute("SELECT * FROM CUSTOMERS")

result2 = db.fetchall()

print("Displaying the table after performing operations:\n")

for y in result2:
    print(y)