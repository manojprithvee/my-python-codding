x1=[1,2,1,2,]
x2=[1,2,2,1]
x3=[1,2,1,2]
def List_prop(q):
	i=0
	temp=0
	max1=0
	max2=0
	min1=0
	flag=''
	for n in q:
		if i==0:
			temp=n
			i=i+1
		else :
			if temp<n:
				temp=n
				i=i+1
				if flag[-3:]!="max":
					flag=flag+"max"
				if flag.find("maxmin"):
					max1=n
				else:
					max2=n
			if temp>n:
				temp=n
				min1=n
				i=i+i
				if flag[-3:]!="min":
					flag=flag+"min"
		ret={"Flag":flag,"max1":max1,"max2":max2,"min1":min1}
	return ret

l=[x1,x2,x3]
i=0
t=''
t1=List_prop(l[i])
print t1
while i<3:
	t1=List_prop(l[i])
	t2=List_prop(l[i+2]) 
	if t1["Flag"]==t2["Flag"] and t2["Flag"]=="maxminmax":
		t3=List_prop(l[i+1])
		if t3["max1"]>3 and t3['Flag']=="maxminmax":
			print "bus"
		elif t3["max1"]<3 and t3['Flag']=="maxmin":
			print "car"
		i=i+3 
	else:
			j=i
			while j<i+2:
				tmp=List_prop(l[j])
				if tmp["Flag"]=="maxmin":
					if tmp["max1"]>2:
						print "scotter"
					elif tmp["max1"]<2:
						print "bike"
				elif tmp['Flag']=="maxminmax":
					print "bicycle"
					j=j+1
	i=i+1	