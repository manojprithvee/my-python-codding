import MySQLdb
import time
db = MySQLdb.connect("localhost","root","123456","trans" )
cursor = db.cursor()
sql = "select * from ramdom"
cursor.execute(sql)
while True:
   	try:
   		result=cursor.fetchone()
   		print result
   	except Exception, e:
   		pass