secret_number = 7
attempts = 0

print("Welcome to the Guess the Number game!")
while True:
    guess = int(input("Take a guess: "))
    attempts += 1 
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break  

