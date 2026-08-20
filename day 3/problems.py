#Take a number from the user and calculate its factorial using a loop.
num= int(input("Enter number "))
factorial = 1
temp = num

if num< 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    while temp > 0:
        factorial *= temp
        temp -= 1
        
    print(f"The factorial of {num} is {factorial}")
 
#Take a positive integer and count how many digits it contains.
num= int(input("Enter number "))
if num == 0:
    print("Digits: 1")
else:
  i=0
  while num>0:
      num//=10
      i+=1
  print("digit : ",i)

#Take a number and calculate the sum of its digits using a loop.
number = int(input("Enter number : "))
digit_sum = 0
while number > 0:
    last_digit = number % 10     
    digit_sum += last_digit      
    number = number // 10        

print("Sum of digits:", digit_sum) 


#Take a number and calculate the sum of its digits using a loop.
number = int(input("Enter number : ")
digit_sum = 0
while number > 0:
    remainder = number % 10     
    reverse_num=(reverse_num*10)+remainder    
    number = number // 10        

print("Sum of digits:", reverse_num) 
