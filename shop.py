L=[]
n=0
while 1:
    item=input("enter the item")
    L.append(item)
    n=input("do you want to continie Y/N")
    if n.lower()=="n":
        break
    elif n.lower()=="y":
        continue
        
print("list is ready")               
L.sort(reverse=True)                       
print(L)
