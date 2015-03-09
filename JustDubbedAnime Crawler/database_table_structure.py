import os, sys
from module.database import database
db=database("localhost","root","","just")
subd = os.listdir('just')
for q in subd: 
	q="CREATE TABLE IF NOT EXISTS `"+q+"` (`episodes` varchar(100) DEFAULT NULL,`mp4star` varchar(100) DEFAULT NULL,`uploadcrazy` varchar(100) DEFAULT NULL,`vidcrazy` varchar(100) DEFAULT NULL,`id` int(11) NOT NULL AUTO_INCREMENT,PRIMARY KEY (`id`))"
	print q
	db.fetch_one_query(q)
del db
