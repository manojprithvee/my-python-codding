import MySQLdb
class database:

	def __init__(self,a,b,c,d):
		try:	
			db = MySQLdb.connect(a,b,c,d)
		except Exception, e:
			print "error in connection"
		try:
			cursor = db.cursor(MySQLdb.cursors.DictCursor)
		except Exception, e:
			print "error in cursor"
	def fetch_all_query(q):
		try:
			cursor.execute(q)
		except:
			print "error with query"
		try:
			result=cursor.fetchall()
			return result
		except Exception, e:
			print "error with retarval"
			return "error"
	def fetch_one_query(q):
		try:
			cursor.execute(q)
		except:
			print "error with query"
		try:
			result=cursor.fetchone()
			return result
		except Exception, e:
			print "error with retarval"
			return "error"

	def __del__(self):
		db.close()



