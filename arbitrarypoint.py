from math import *
X,Y=map(int,input("enter the coordinates of center of circle").split())
x,y=map(int,input("enter the coordinates of point").split())
r=int(input('enter the radius of circle'))
a=int((x-X)*2+(y-Y)*2)
d=int(sqrt(a))
if d<r:
	print("point is in the intrior of circle")
elif d==r:
	print("point is on the circle")
else:
	print("point is in exterior of circle")
	
