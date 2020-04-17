n1=3
n2=5
list=[]
counter=1
x1=1
x2=1
while x1<30 or x2<30:
 if counter%n1==0:
      x1=n1*counter
      list.append(x1)
  elif counter%n2==0:
      x2=n2*counter
      list.append(x2)
  else:
      x1=counter*n1
      x2=counter*n2
      if (x1>30 or x2>30):
         list.append(x1)
         list.append(x2)
         break
counter+=1
print list
