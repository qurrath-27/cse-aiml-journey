# Simple ATM

balance = 10000

print("1. Check balance")
print("2. Deposit")
print("3. Withdraw")

choice = int(input("Enter a choice: "))

if choice == 1:
    print("Your balance is:", balance)

elif choice == 2:
    amount = int(input("Amount to be deposited: "))

    if amount > 0:
        balance = balance + amount
        print("Deposit successful")
        print("Current balance:", balance)
    else:
        print("Invalid amount")

elif choice == 3:
    withdrawal_amount = int(input("Enter withdrawal amount: "))

    if withdrawal_amount > 0 and withdrawal_amount <= balance:
        balance = balance - withdrawal_amount
        print("Withdrawal successful")
        print("Remaining balance:", balance)
    else:
        print("Invalid amount")

else:
    print("Invalid choice")