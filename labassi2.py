#Calendar
import calendar
year= int(input("enter the year: "))
month= int(input("enter the month: "))
day= int(input("Enter the day: "))
print(calendar.month(year,month))
#Checking a Leap Year
print("Checking a leap year ")
year=int(input("Enter the year you want to check "))
if year%4==0 or year%400==0:
    print(f"The year {year} is a Leap year")
else:
    print(f"The year {year} is nat a leap year")
#Factorial
print("Factorial of a number")
n=int(input("Enter the number you want to get factorial of "))
fac=1
if n>0:
    for i in range(1,n+1):
        fac=fac*i
    print(f"The factorial of {n} is {fac}")
elif n==0:
    print(f"The factorial of {n} is 1")
else:
    print("The number is -ve")
#Displaying the table
print("displaying the multiplication table")
num=int(input("The number you want table of "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")
#Fibonacci series
number=int(input("The number upto which you fibonacci series upto "))
a=0
b=1
c=1
if number<0:
    print("your number is zero")
elif number==0 or number == 1:
    print(f"The fibonacci series of {number} is {a}")
else:
     for i in range(2,number+1):
         c=a+b
         a=b
         b=c
print(f"the fibonacci series output of {number} is {c}")
#Sum of natural numbers
x=int(input("The number upto which you want the sum "))
s=0
if x<0:
    print(f"The number {x} is -ve")
else:
    for i in range(0,x+1):
        s=s+i
    print(f"The sum upto {x} is {s}")