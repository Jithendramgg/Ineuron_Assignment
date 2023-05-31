# Question 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
num = int(input("Enter a number: "))
if(num > 0):
    print(num, "is Positive")
elif(num < 0):
    print(num, "is Negative")
else:
    print(num, "is Zero")
#Question 2. Write a Python Program to Check if a Number is Odd or Even?
num = int(input("Enter a number: "))

if(num % 2 == 0):
    print(num, "is a Even Nummber")
else:
    print(num, "is an Odd Number")

#Question 3. Write a Python Program to Check Leap Year?

year = int(input("Enter a year: "))

if(((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
    print("Leap Year")
else:
    print("Not a Leap Year")
    
#Question 4. Write a Python Program to Check Prime Number?
num = int(input("Enter a number: "))

isPrime = True

if num <= 1:
    print(num, "is neither prime nor composite")
else:
    d = 2
    while(d*d <= num):
        if(num%d==0):
            isPrime = False
            break
        d = d + 1

if(num > 1):
    if(isPrime):
        print(num, "is prime number")
    else:
        print(num, "is not prime number")
#Question 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000

for num in range(1, 10001):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
