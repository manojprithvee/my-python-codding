import os, sys,time
from module.database import database
db=database("localhost","root","","just")
subd = os.listdir('just')
for q in subd: 
	q="CREATE TABLE IF NOT EXISTS `"+q+"` (`episodes` varchar(100) DEFAULT NULL,`mp4star` varchar(100) DEFAULT NULL,`uploadcrazy` varchar(100) DEFAULT NULL,`vidcrazy` varchar(100) DEFAULT NULL,`id` int(11) NOT NULL AUTO_INCREMENT,PRIMARY KEY (`id`))"
	print q
	db.fetch_one_query(q)
for s in subd:
	ert=s
	files=os.listdir("just/"+s)
	for fi in files:
		flist=[]
		flist.append(fi)
		f=open("just/"+s+"/"+fi)
		con=f.read()
		f.close()
		con=con.splitlines()
		for c in con:
			c=c.replace(";bg=http://i.imgur.com/4k5MU.jpg","")
			flist.append(c)
		try:
			query="INSERT INTO "+"`"+ert+"`"+" (`episodes`, `mp4star`, `uploadcrazy`, `vidcrazy`) VALUES "+"('"+flist[0]+"','"+flist[1]+"','"+flist[2]+"','"+flist[3]+"')"
			print query
			db.fetch_one_query(query)
		except:
			query="INSERT INTO "+"`"+ert+"`"+" (`episodes`, `mp4star`) VALUES "+"('"+flist[0]+"','"+flist[1]+"')"
			print query
			db.fetch_one_query(query);
del db