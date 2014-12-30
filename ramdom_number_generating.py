import random
a=open("number.txt","a")
i=100
raw_input("manoj:")
while i>=1:
	q=random.randint(100000, 999999)
	q=str(q)+"\n"
	a.write(q)
	i=i-1
a.close()
