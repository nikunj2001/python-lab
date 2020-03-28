a='''splits abcs apples bat car dar numbers'''
b=a.split()
for i in b:
	if i.endswith('s'):
		print(i)
	else:
		pass