import urllib2
import libxml2

i=1000000
srt=""
while i<=9999999:
	url='http://www.svce.ac.in/departments/it/profile/fac.php?id=IT'+str(i)
	print url
	f = urllib2.urlopen(url)
	html = f.read()
	f.close()
	parse_options = libxml2.HTML_PARSE_RECOVER + \
	libxml2.HTML_PARSE_NOERROR + \
	libxml2.HTML_PARSE_NOWARNING
	doc = libxml2.htmlReadDoc(html,'',None,parse_options)
	if str(html).find("Error quering database")>=0:
		i=i+1
	else:	
		div = doc.xpathEval('//div[@id="courseContent"]/font/ul/li/text()')
		if not div:
			div = doc.xpathEval('//inden/text()')
		if not div:
			div = doc.xpathEval('//div[@id="courseContent"]/ol/li/text()') 
		if not div:
			div = doc.xpathEval('//div[@id="courseContent"]/ul/li/text()') 
		if not div:
			div = doc.xpathEval('//div[@id="courseContent"]/li/text()') 
		if not div:
			div = doc.xpathEval('//div[@id="courseContent"]/font/li/text()') 
		if not div:
			div = doc.xpathEval('//div[@id="courseContent"]/text()') 
		if not div:
			div = doc.xpathEval('//div') 
		name=doc.xpathEval('//title/text()')
		srt= srt+"Name : "+str(name[0]).strip().replace("SVCE | Department OF CSE | Faculty Profile - ","").replace("SVCE | Department OF TSE | Faculty Profile - ","")+"     "+"\n"
		srt=srt+"course taken:\n"
		for ij in div:
			srt=srt+'\t'+str(ij).strip()+"\n"
		srt=srt+ "------------------------------------------------------------------------------------------------------------"+"\n"
		doc.freeDoc()
		i=i+1
fileh=open("staff.txt","w")
fileh.write(srt.replace("\n\n","\n"))
