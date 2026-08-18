#Take a 3-digit number and calculate the sum of its digits.
number=int(input("enter a 3 digit number :"))
a=number%10
m=number//10
b=m%10
c=m//10
print("the sum of digits are " , a+b+c)

