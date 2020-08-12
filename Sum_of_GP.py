# Python Program to find Sum of Geometric Progression Series
import math

def sumofGP(a, n, r):
    total = (a * (1 - math.pow(r, n ))) / (1- r)
    return total

a = int(input("Please Enter First Number of an G.P Series: : "))
n = int(input("Please Enter the Total Numbers in this G.P Series: : "))
r = int(input("Please Enter the Common Ratio : "))

total = sumofGP(a, n, r)
print("\nThe Sum of Geometric Progression Series = " , total)
