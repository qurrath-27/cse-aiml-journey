#take a name as input and print First character,Last character,Length of name
name = input("Enter a name:")
print(name[0])
print(name[-1])
print(len(name))

#Take a string and print it:Uppercase,Lowercase,Reversed
name = input("Enter a name:")
print(name.upper())
print(name.lower())
print(name[::-1])

#Take a sentence and count how many vowels it contains.
name = input("Enter a sentence:")
vowels = "aeiouAEIOU"
count=0
for c in name:
 if c in vowels:
   count+=1
print(count)

#Take a string and count::vowels, consonants ,digits ,spaces.
name = input("Enter a sentence:")
vowels = "aeiouAEIOU"
space=" "
consonants="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
digits="0123456789"
v_count = 0
c_count = 0
d_count = 0
s_count = 0
sc_count = 0
for char in name:
 if char in vowels:
     v_count+=1
 elif char in space:
    s_count+=1
 elif char in digits:
    d_count+=1
 elif char in consonants:
    c_count+=1
 else:
    sc_count+=1
print("Vowels:", v_count)
print("Consonants:", c_count)
print("Digits:", d_count)
print("Spaces:", s_count)
print("Special characters:", sc_count)

#Then use a loop to calculate::Each number,Total,Average
numbers=[10,20,30,40,50]
for number in numbers:
 print(number)
total=0
for number in numbers:
 total+=number
print(total)
print("average : " ,total/len(numbers))

#Take 5 numbers from the user, store them in a list, and find the largest number.
numbers = []

for i in range(5):
    val = int(input(f"Enter number {i + 1}: "))
    numbers.append(val)

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("The list of numbers is:", numbers)
print("The largest number is:", largest)


numbers = []
for i in range(5):
  num = int(input(f"Enter number {i+1}: "))
  numbers.append(num)
even_numbers = []
odd_numbers = []
for num in numbers:
  if num % 2 == 0:
    even_numbers.append(num)
  else:
    odd_numbers.append(num)
print("Original List:", numbers)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)





numbers = []
for i in range(5):
  num = int(input(f"Enter number {i+1}: "))
  numbers.append(num)
even_numbers = []
for num in numbers:
  if num % 2 == 0:
    even_numbers.append(num)
total=0
for num in even_numbers:
  total+=num
print("Even numbers:", even_numbers)
print("sum of even", total)


numbers = []

for i in range(5):
    val = int(input(f"Enter number {i + 1}: "))
    numbers.append(val)

largest = numbers[0]
second largest=numbers[1]
for num in numbers:
    if num > largest:
        largest = num

print("The list of numbers is:", numbers)
print("The largest number is:", largest)


   
