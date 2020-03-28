a='''the tiger the lion the himalya the nikunj'''
b=a.split()
print(b)
c=0
for i in b:
	if i=='the':
		c+=1
print(c)