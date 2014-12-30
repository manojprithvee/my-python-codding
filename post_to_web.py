import requests
import codecs
from lxml import html
import urllib2
import libxml2
i=1
srt=""
request = requests.get('http://www.svce.ac.in/departments/cse/profile/fac.php')
print request
	