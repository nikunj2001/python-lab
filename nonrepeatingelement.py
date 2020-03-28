a='nikunj'
b=list(a)
c=[]
for i in b:
	if i not in c:
		c.append(i)
for i in c:
	print(i,end='')