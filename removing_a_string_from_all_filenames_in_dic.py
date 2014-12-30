import os

count=0
man='www.TamilRockers.com - '#enter the string tobe replaced
for path, subdirs, files in os.walk('/home/manoj/Videos/movies'):#enter the full path
	for filename in subdirs:
		if man in filename:
			filename1=filename.replace(man,"")
			os.rename(os.path.join(path, filename),os.path.join(path, filename1))
			count=count+1
print count
