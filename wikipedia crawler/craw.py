import urllib2
import libxml2
import os
import pdfkit
def craw(url):
	#url='https://en.wikipedia.org/wiki/Main_Page'
	hdr = {'User-Agent':'Mozilla/5.0'}
	req = urllib2.Request(url,headers=hdr)
	f = urllib2.urlopen(req)
	html = f.read()
	f.close()
	parse_options = libxml2.HTML_PARSE_RECOVER + \
	libxml2.HTML_PARSE_NOERROR + \
	libxml2.HTML_PARSE_NOWARNING
	doc = libxml2.htmlReadDoc(html,'',None,parse_options)
	man=doc.xpathEval('//title/text()')
	t=""
	for x in man:
		t=x
	f=open(str(t),'w')
	f.write(html)
	print t
	epview=doc.xpathEval('//a/@href')
	for a in epview:
		if str(a).find("//")!=-1 or str(a).find("#")!=-1:
			pass
			#print 'https:'+str(a).replace('"','').replace("href=","").replace(" ","")
		else:
			q="https://en.wikipedia.org"+str(a).replace('"','').replace("href=","").replace(" ","")
			print q
			craw(q)
craw('https://en.wikipedia.org/wiki/Main_Page')