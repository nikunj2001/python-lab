a='nikunj6789'
b=list(a)
c=[]
for i in b:
	if ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122:
		c.append(i)
for i in c:
	print(i,end='')