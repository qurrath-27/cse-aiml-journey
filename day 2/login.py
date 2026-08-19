#Create a simple login system.
correct_name="right"
correct_pw="123"
username = input("Enter username :")
Password = input("enter password :")
if username==correct_name and Password==correct_pw:
 print("Login successful")
else:
 print("Invalid username or password")