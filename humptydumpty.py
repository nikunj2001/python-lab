def hd(a):
	if a%3==0 and a%5==0:
		return('humpty_dumpty')
	elif a%5==0:
		return('dumpty')
	elif a%3==0:
		return('humpty')
		
	











x=int(input('enter a number to be checked'))
r=hd(x)
print(r)