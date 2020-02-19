T=()
n=int(input())
for i in range (n) :
	d=input()
	if d.isalpha():
		T+=(d,)
	else:
		T+=(eval(d),)
print(T)

