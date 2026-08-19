#Take marks as input.90–100 → A80–89  → B70–79  → C60–69  → D40–59  → EBelow 40 → Fail
marks=int(input("Enter marks : "))
if  marks >=90 :
 print("A")
elif  marks >= 80 :
 print("B")
elif  marks >= 70 :
 print("C")
elif  marks >= 60 :
 print("D")
elif  marks >= 40:
 print("E")
else:
 print("Fail")

#Take three numbers and find the largest.
a = float(input("Enter number 1 : "))
b = float(input("Enter number 2 : "))
c = float(input("Enter number 3 : "))
if a>=b and a>=c:
 print(a , " is largest ")
elif b>=a and b>=c:
 print(b , " is largest ")
else:
 print(c , " is largest ")


#Check whether a year is a leap year.
year = int(input("Enter year : "))
if year%400==0 or (year%4==0 and year%100!=0):
 print("leap year")
else:
 print("Not a leap year")