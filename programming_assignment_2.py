# Question 1. Write a Python program to convert kilometers to miles
kms = 10
miles = kms/1.61
print("for kms {} in miles is {}".format(kms,miles))

#Question 2. Write a Python program to convert Celsius to Fahrenheit
C= 35
F = (9*C/5)+32
print("{} Celsius in Fahrenheit is {}".format(C,F))

#Question 3. Write a Python program to display calendar
import calendar
print(calendar.month(2023,5))

#Question 4. Write a Python program to solve quadratic equation
import math

print("ax^2 + bx^1 + c = 0")
print("Enter the coeff a, b and constant c")

a = int(input(("Enter the coeff a: ")))
b = int(input(("Enter the coeff b: ")))
c = int(input(("Enter the constant c: ")))
print(math.sqrt(2))
d = (b**2) - (4*a*c)
if d>=0:
    root1 = (((-1*b)+(math.sqrt(d))) / (2*a))
    root2 = (((-1*b)-(math.sqrt(d))) / (2*a))
if d<0:
    d= -d
    root1 = (((-1*b)+(math.sqrt(d))) / (2*a))
    root2 = (((-1*b)-(math.sqrt(d))) / (2*a))
print('\nFor quad eq. {}x^2 + ({})x^1 + {}'.format(a,b,c))
print('The solutions are: {} and {}'.format(root1, root2))

#Question 5.Write a Python program to swap two variables without temp variable

var1 = 6
var2 = 4

print('Before swap:\nvar1 = {} and var2 = {}'.format(var1, var2))
var2 = var1 + var2
var1 = var2 - var1
var2 = var2 - var1

print('\nAfter swap:\nvar1 = {} and var2 = {}'.format(var1, var2))
