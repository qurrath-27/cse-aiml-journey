#Take a number and determine whether it is:positive,negative,zero
a = float(input("Enter a number : "))
if a > 0 :
   print( a ," is positive number")
elif a < 0:
   print( a ," is negative number")
else :
 print(a, "is zero")

#Take a number and determine whether it is:even or odd
num = int(input("Enter a number : "))
if num%2==0:
  print(f"{num} is even")
else:
  print(f"{num} is odd")

#Take two numbers and print the larger number.
a = float(input("Enter a number : "))
b = float(input("Enter another number : "))
if a>b:
  print(f"{a} is greater than {b}")
elif a<b:
  print(f"{b} is greater than {a}")
else:
  print("both are equal")


#Take a person's age: Child→ below 13,Teenager→ 13–19,Adult→ 20+
age = int(input("enter your age : "))
if age < 13:
 print("child")
elif 13 <= age <=19:
 print("teenager")
else:
 print("adult")
