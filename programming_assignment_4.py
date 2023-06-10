# Question 1. Write a Python Program to Find the Factorial of a Number?

num=int(input("Enter a Value for factorial "))
s=1
if num<=0:
    s=1
else:
    for i in range(1,num+1):
        s=s*i
print("factotial of input {} is {}".format(num,s))
    
#Question 2. Write a Python Program to Display the multiplication Table

num=int(input("Enter a Value for Table "))
for i in range(1,11):
    print("{} x {} = {}".format(num,i,num*i))
    
#Question 3. Write a Python Program to Print the Fibonacci sequence?

num=int(input("Enter a length for fibinacci "))
a=0
b=1
if num==1: print(a)
elif num==2:
    print(a) 
    print(b)
else:
    print(a)
    print(b)
    while (num-2)>0:
        nt=a+b
        print(a+b)
        b=nt
        a=b
        num-=1
    
#Question 4. Write a Python Program to Check Armstrong Number
import math
num=int(input("Enter a number to check if it is Armstrong Number "))
l = len(str(num))  ## l = number of digits of number
sum1 = 0 
temp_num = num
while(num > 0):
        d = num % 10
        sum1 += int(math.pow(d, l))
        num = num // 10

if(sum1 == int(temp_num)):
        print("It is Armstrong Number")
else:
        print("It is not Armstrong Number")
#Question 5. Write a Python Program to Find Armstrong Number in an Interval?

import math

r1=int(input("Lowest range of Amstrong you want "))
r2=int(input("Highest range of Amstrong you want "))
for i in range(r1,r2):
    l = len(str(i))  ## l = number of digits of number
    sum1 = 0 
    temp_num = i
    while(i > 0):
        d = i % 10
        sum1 += int(math.pow(d, l))
        i = i // 10

    if(sum1 == int(temp_num)):
        print(temp_num , " ")
 
 #Question6. Write a Python Program to Find the Sum of Natural Numbers
num = int(input("Enter a positive number: "))
s=(num*(num+1))//2
print(s)
    