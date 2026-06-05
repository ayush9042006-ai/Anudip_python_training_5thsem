balance = 10000
 
while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
 
    choice = int(input("Enter your choice: "))
 
    if choice == 1:
        print(f"Current Balance: ₹{balance}")
 
    elif choice == 2:
        amount = float(input("Enter deposit amount: ₹"))
        balance += amount
        print(f"₹{amount} deposited successfully.")
        print(f"Updated Balance: ₹{balance}")
 
    elif choice == 3:
        amount = float(input("Enter withdrawal amount: ₹"))
 
        if amount <= balance:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining Balance: ₹{balance}")
        else:
            print("Insufficient balance! Withdrawal failed.")
 
    elif choice == 4:
        print("Thank you for using the ATM.")
        break
 
    else:
        print("Invalid choice! Please try again.")