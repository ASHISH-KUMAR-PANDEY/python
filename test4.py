#program to find AREA of triangle
a=float(input('Enter side a:'))
b=float(input('Enter side b:'))
c=float(input('Enter side c:'))
s=(a+b+c)/2
print(s)
area= (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
