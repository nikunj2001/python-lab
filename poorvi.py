for i in range(7):
	for j in range(5):
		if ((j==0 or (j==4 and (i>0 and i<3)) or ((i==0 or i==3) and (j>0 or j<4)))):
			print("*",end='')
		else:
			print(end=" ")
	print()
for i in range(2):
	print()
for i in range(7):
	for j in range(5):
		if ((j==0 or j==4) or ((i==0 or i==6) and (j>0 or j<4))):
			print("*",end="")
		else:
			print(end=" ")
	print()
for i in range(2):
	print()
for i in range(7):
	for j in range(5):
		if ((j==0 or j==4) or ((i==0 or i==6) and (j>0 or j<4))):
			print("*",end="")
		else:
			print(end=" ")
	print()
for i in range(2):
	print()
for i in range(7):
	for j in range(5):
		if ((j==0 or (j==4 and (i>0 and i<3))) or ((i==0 or i==3) and (j>0 or j<4))):
			print("*",end='')
		elif ((i==4 and j==1) or (i==5 and j==2) or (i==6 and j==3) ):
			print('*',end='')
		else:
			print(end=" ")
	print()
for i in range(2):
	print()
a=0
b=6
for i in range(4):
	for j in range(9):
		if i==j:
			print('*',end='')
		elif i==a and j==b:
			print("*",end='')
			a=a+1
			b=b-1
		else:
			print(end=" ")
	print()
for i in range(2):
	print()
for i in range(7):
	for j in range(5):
		if ((i==0 or i==6) or (j==2 and (i>0 or i<6))):
			print('*',end='')
		else:
			print(end=" ")
	print()