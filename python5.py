l=("nikunj",1,2,3,5)
a=list(l)
n=int(input('enter the number of  elements to be added:'))
for i in range(n):
	e=input("enter the element to be added")
	a.append(e)
print(tuple(a))

