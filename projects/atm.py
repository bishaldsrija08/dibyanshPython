# Project III (ATM Simulator in Python)
amount = 0

def atm():
    global amount
    print("Welcome to the ATM Simulator!")
    print("Please select an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    
    while True:
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            print(f"Your current balance is: ${amount:.2f}")
        elif choice == '2':
            deposit = float(input("Enter the amount to deposit: "))
            if deposit > 0:
                amount += deposit
                print(f"${deposit:.2f} deposited successfully.")
            else:
                print("Invalid deposit amount. Please try again.")
        elif choice == '3':
            withdraw = float(input("Enter the amount to withdraw: "))
            if 0 < withdraw <= amount:
                amount -= withdraw
                print(f"${withdraw:.2f} withdrawn successfully.")
            else:
                print("Invalid withdrawal amount. Please try again.")
        else:
            print("Invalid choice. Please select a valid option (1-3).")

atm()