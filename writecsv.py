import csv,time
i=0
reg=list()
name=list()
attence=list()
with open('test.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE)
    for row in reader:
        reg.append(row[0])
        attence.append(0)
import Tkinter
from Tkinter import *
def onclick():
	i=0
	output=""
	fileh=open('test.csv', 'rb')
	a=fileh.read()
	q=a.splitlines()
	fileh.close()
	for row in q:
		if (i==0):
			row=str(row)+','+time.strftime("%d/%m/%Y")
		else:
			d=9;	
			if (attence[i].get()==1):
				d=0
			else:
				d=1
			row=str(row)+','+str(d)
		output=output+row+"\n"
		i=i+1
	fileh=open('test.csv','w')
	fileh.write(output)
	fileh.close()
	f = open('test1.csv')
	csv_f = csv.reader(f)
	output=''
	i=1
	for row in csv_f:
		print row
  		row[1]=str(int(row[1])+1)
  		row[2]=str(int (row[2])+attence[i].get())
  		output=output+row[0]+","+row[1]+","+row[2]+'\n'
  	fileh=open('test1.csv','w')
	fileh.write(output)
	fileh.close()
	f.close()


	

top = Tkinter.Tk()
top.grid()
c=0
lis=[1,2,3,4,5,6,7,8,9,10]
for r in reg:
		if(i==0):
			attence[i]=0
			i=i+1
		else:
			ro=i-1
			print i;
			attence[i]=IntVar()
			Label(top, text=r).grid(row=((ro%10)+1),column=c)
			Checkbutton(top, variable = attence[i],onvalue = 1,offvalue = 0).grid(row=((ro%10)+1),column=c+1)
			if(ro%10+1==10):
				c=c+2;
			i=i+1
Button(top, text ="Hello", command = onclick).grid(row=11,column=(c/2))
top.mainloop()