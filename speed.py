def speed(x):
	c=0
	if x<=70:
		return('ok')
	elif x>70:
		d=x-70
		a=d//5
		m=c+a*2
		if m>=12:
			return('lisence suspended',m)
		else:
			return('over speeding',m)
a=int(input('enter speed'))
r=speed(a)
print(r)
		
		

	