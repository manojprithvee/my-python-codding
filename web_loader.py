import thread
import time
import urllib2

def print_time( threadName):
	i=0
	print "%s: %s" % ( threadName, time.ctime(time.time()) )
	while True:
		url='http://www.svce.ac.in'
		print threadName+"-"+(str(i))
		f = urllib2.urlopen(url)
		html = f.read()
		i=i+1
		
		

# Create two threads as follows
try:
	thread.start_new_thread( print_time, ("Thread-1",) )
	thread.start_new_thread( print_time, ("Thread-2",) )
	thread.start_new_thread( print_time, ("Thread-3",) )
	thread.start_new_thread( print_time, ("Thread-4",) )
	thread.start_new_thread( print_time, ("Thread-5",) )
	thread.start_new_thread( print_time, ("Thread-6",) )
	thread.start_new_thread( print_time, ("Thread-7",) )
	thread.start_new_thread( print_time, ("Thread-8",) )
	thread.start_new_thread( print_time, ("Thread-9",) )
	thread.start_new_thread( print_time, ("Thread-10",) )
	thread.start_new_thread( print_time, ("Thread-11",) )
	thread.start_new_thread( print_time, ("Thread-12",) )
	thread.start_new_thread( print_time, ("Thread-13",) )
except:
	print "Error: unable to start thread"

while 1:
	pass