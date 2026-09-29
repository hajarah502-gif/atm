# Simple Python ATM

# Step 1: Set up variables
pin = 1234
balance = 100000
attempts = 0

# Step 2: Ask for the PIN
while attempts < 3:
    entered_pin = int(input("Enter your PIN: "))

    if entered_pin == pin:
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Wrong PIN!")
        print("You have", 3 - attempts, "attempt(s) left.")

# Check if the card should be blocked
if attempts == 3:
    print("Card blocked!")
else:

    # Step 3: Show the continuous menu
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        # Step 4: Handle the choices
        if choice == '1':
            print("Your current balance is:", balance)

        elif choice == '2':
            # Step 5: Deposit
            amount = float(input("Enter amount to deposit: "))

            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print("New balance:", balance)
            else:
                print("Error: Deposit amount must be greater than zero.")

        elif choice == '3':
            # Step 5: Withdrawal
            amount = float(input("Enter amount to withdraw: "))

            if amount <= 0:
                print("Error: Enter an amount greater than 0.")
            elif amount > balance:
                print("Error: You do not have enough money!")
            else:
                balance -= amount
                print("Cash dispensed:", amount)
                print("New balance:", balance)

        elif choice == '4':
            print("Thank you, goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")