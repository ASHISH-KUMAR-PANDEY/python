import time

#importing fractions module
from fractions import Fraction

#time at the start of program execution
start = time.time()

#Product of all the four fractions say 1 for now
product = 1

#'for' loops to generate Numerator and Denominator
for i in xrange(10,100):
	for j in xrange(i+1,100):
		#Intersection of Two sets(Common number between the two)
		common = list(set(str(i))&set(str(j)))
		#Check if the list is not empty
		if len(common) != 0:
			#Check if the common number is not 0
			if common[0] != '0':
				num = list(str(i))
				den = list(str(j))
				#Remove the common element from numerator
				num.remove(common[0])
				#Remove the common element from Denominator
				den.remove(common[0])
				#Check if the value of num and den are not equal to 0
				if num[0]!='0' and den[0]!='0':
					#Check if they satisfy the question condition
					if Fraction(int(num[0]),int(den[0])) == Fraction(i,j):
						#multiply to the product
						product *= Fraction(i,j)

#print the denominator of the resulting fraction
print product.denominator

#time at the end of program execution
end = time.time()

#Printing the total time for execution
print end - start
