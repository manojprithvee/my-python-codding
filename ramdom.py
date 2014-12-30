
import MySQLdb
import random
db = MySQLdb.connect("localhost","root","123456","trans" )
cursor = db.cursor()
i=0
while True:
   sql = "insert into ramdom values ("+str(random.randint(100000, 999999))+")"
   print sql
   cursor.execute(sql)
   i=i+1
   db.commit()
db.close()
