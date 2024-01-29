# CSCI1010: Lab 1, Problem 1
# Filename: hw1pr2.py
# Name: Rashidat Popoola Aromire 
# Problem description: Solving the quadratic equation!

import cmath 

a = input('Enter a value for a:')
b = input ('Enter a value for b: ')
c = input ('Enter a value for c: ')

a = float(a)
b = float(b)
c = float(c)

#finding the determinant 
d = (b**2) - (4*a*c)

s1 = ((-b-cmath.sqrt(d))/(2*a))
s2 = ((-b+cmath.sqrt(d))/(2*a))

print('The solutions are: ', s1,s2)
