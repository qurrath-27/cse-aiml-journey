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