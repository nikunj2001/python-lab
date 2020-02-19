t=(1,2,3,4,5,2)
c=0
b=[]
for i in t:
	t.count(i)
	c+=1
	if c>1:
		b.append(i)
print(b)
	
