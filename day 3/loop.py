#Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
   print(i)

#Print all even numbers from 1 to 50.
for i in range(2,51,2):
  print(i)

#Print all odd numbers from 1 to 50.
for  i in range(1,51,2):
  print(i)

#Take a number from the user and print its multiplication table.
num=int(input("Enter  number: "))
for i in range(1,11):
 print(num ," * ", i ," = " , num*i)

#Take n from the user and calculate: 1 + 2 + 3 + ... + n(no formula)
n= int(input("Enter number "))
total = 0
i= 1
while i <= n:
   total+=i
   i += 1
print("total sum : ",total)
