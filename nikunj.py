for i in range(5):
	for  j in range(5):
		if ((j==0 or j==4) or (i==j)):
			print("*",end='')
		else:
			print(end=" ")
	print()
for i in range(2):
	print()
for i in range(5):
	for  j in range(5):
		if ((i==0 or i==4) or j==2):
			print("*",end='')
		else:
			print(end=" ")
	print()
for i in range(2):
	print()
a=3
b=2



for i in range(5):
	for  j in range(5):
		if (j==0):
			print("*",end='')
		elif(a==i and b==j):
			
			print("*",end="")
			a=a+1
			b=b+1
		elif((i==2 and j==1) or (i==1 and j==2) or (i==0 and j==3)):
			print("*",end="")
			
		else:
			print(end=" ")
	print()
for i in range(2):
	print()
for i in range(5):
	for  j in range(5):
		if ((j==0 or j==4) or i==4):
			print("*",end='')
		else:
			print(end=" ")
	print()
for i in range(2):
	print()
for i in range(5):
	for  j in range(5):
		if ((j==0 or j==4) or (i==j)):
			print("*",end='')
		else:
			print(end=" ")
	print()
for i in range(2):
	print()
for i in range(5):
	for  j in range(5):
		if ((i==0) or (j==2) or (i==4 and (j>=0 and j<=2)) or (j==0 and (i>2 and i<5))):
			print("*",end='')
		else:
			print(end=" ")
	print()
	