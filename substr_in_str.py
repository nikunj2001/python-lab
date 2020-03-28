a='''the nikunj gupta the nikunj'''
b=a.split()
c='nikunj'
n=0
for i in b:
	if i==c:
		n+=1
if n>=1:
	print('yes',n)
else:
	print('no')