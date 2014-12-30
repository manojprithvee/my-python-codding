import binascii
import base64
filea=open("read.txt","rb")
a=filea.read()
print binascii.a2b_base64(a)
filea.close()
filea=open("write.txt","a")
i=50
while i>=0:
	filea.write("manojis a good boy\n")
	i=i-1
filea.close()
