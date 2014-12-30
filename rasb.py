import json
import MySQLdb
from requests import session
a=False
def send_switch_init_id(auth,a,a_status):
	json_string={"auth":auth,"switch":a,"switch_status":a_status}
	string=json.dump(json_string)
	payload = {
    'json': string
	}
	with session() as c:
    	c.post('http://chinnarajutraders.t15.org/login.php', data=payload)
def send_switch_id(auth,a):
	json_string={"auth":auth,"switch":a}
	string=json.dump(json_string)
	with session() as c:
 		c.post('http://chinnarajutraders.t15.org/login.php', data=string)
def db_update(a,switch_status):
	db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
	cursor = db.cursor()
	sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)
	try:
		cursor.execute(sql)
	except:
   		print "Error: unable to fecth data"
	db.close()
def get_data_server(auth,a):
	with session() as c:
		url=''
		authid="auth="+auth+"&"
		swit="switch="+a
		url=url+authid+swit
    	request = c.get(url)
    	db_update(a,request)


