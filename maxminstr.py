a='nikunj'
b=list(a)
c=[]
for i in b:
	c.append(ord(i))
c.sort()
ma=max(c)
mi=min(c)
print(chr(ma))
print(chr(mi))