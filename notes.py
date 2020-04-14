a=int(input("enter the amount you have"))
b=a//2000
c=a-b*2000
if c>500:
	d=c//500
	e=c-d*500
	f=e//100
	print(f"2000={b} 500={d} 100={f}")
elif c<=500:
	h=c//100
	print(f"2000={b} 500=0 100={h}")
