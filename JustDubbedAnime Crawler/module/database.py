import MySQLdb
class database:
	cursor=None
	db=None
	def __init__(self,a,b,c,d):
		try:
			self.db = MySQLdb.connect(a,b,c,d)
		except Exception, e :
			print "error in connection",e
		try:
			self.cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
		except Exception, e :
			print "error in cursor",e
	def fetch_all_query(self,q):
		try:
			self.cursor.execute(q)
		except Exception, e:
			print "error with query",e
		try:
			result=self.cursor.fetchall()
			return result
		except Exception, e :
			print "error with retarval",e
			return "error"
	def fetch_one_query(self,q):
		try:
			self.cursor.execute(q)
			self.db.commit()
		except Exception, e:
			print "error with query",e
		try:
			result=self.cursor.fetchone()
			return result
		except Exception, e:
			print "error with retarval",e
			return "error"

	def __del__(self):
		self.db.close()
