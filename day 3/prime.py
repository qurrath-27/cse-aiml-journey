#Take a number and determine whether it is prime.
num = int(input("Enter a number: "))
if num <= 1:
    print(f"{num} is not a prime number.")
else:
    divisor = 2
    is_prime = True
    while divisor <= (num // 2):
        if num % divisor == 0:
            is_prime = False  
            break  
        divisor += 1  
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")


 
