x=int(input('total shopping amount'))
if  x>=25000:
	print("GOLD")
	a=(x/100)*20
	t=x-a
	print(f'Total amount to be paid Rs.{t}')
elif x>=10000 and x<25000:
	print('SILVER')
	a=(x/100)*15
	t=x-a
	print('Total amount to be paid Rs.{t}')
else:
	print('BRONZE')
	a=(x/100)*10
	t=x-a
	print('Total amount to be paid Rs.{t}')
	