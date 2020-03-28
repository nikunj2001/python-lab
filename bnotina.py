a='abcdef'
b='efghijk'
c=list(a)
d=list(b)
e=list(i for i in b if i not in a)
print(e)