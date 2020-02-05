for i in range(4):
   for j in range(4):
      if i==j>0 or i==j<3 or i+j==3:
          print(" ",end="")
      else:
         print("*",end="")    
   print()   
