d=list(map(int,input('enter the date in the format of dd/mm/yyyy: ').split('/')))
a=len(d)
for i in range(a):
	b=d[0]
	m=d[1]
	x=d[2]
	break
if x%4==0:
	if x%100==0:
		if x%400==0:
			y='ly'
		else:
			y='ny'
	else:
		y='ly'
else:
	y='ny'
if y=='ly':
	feb=29
	t=366
elif y=='ny':
	feb=28
	t=365
if int(m)==1:
	l=t-b
	print(f'days left in year {l}')
elif int(m)==2:
	l=t-(31+b)
	print(f'days left in year {l}')
elif int(m)==3:
	l=t-(31+feb+b)
	print(f'days left in year {l}')
elif int(m)==4:
	l=t-(2*31+feb+b)
	print(f'days left in year {l}')
elif int(m)==5:
	l=t-(2*31+feb+30+b)
	print(f'days left in year {l}')
elif int(m)==6:
	l=t-(3*31+feb+30+b)
	print(f'days left in year {l}')
elif int(m)==7:
	l=t-(3*31+feb+30*2+b)
	print(f'days left in year {l}')
elif int(m)==8:
	l=t-(4*31+30*2+feb+b)
	print(f'days left in year {l}')
elif int(m)==9:
	l=t-(5*31+30*2+feb+b)
	print(f'days left in year {l}')
elif int(m)==10:
	l=t-(5*31+30*3+feb+b)
	print(f'days left in year {l}')
elif int(m)==11:
	l=t-(6*31+30*3+feb+b)
	print(f'days left in year {l}')
elif int(m)==12:
	l=t-(6*31+30*4+feb+b)
	print(f'days left in year {l}')
	