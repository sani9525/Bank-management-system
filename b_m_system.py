# Bank management system

def show_balance():
    print("*******************")
    print(f"Your balance is ₹ {balance:.2f}")

def deposit():
    print("*******************")
    amount=float(input("Enter an amount to be deposited ₹: "))

    if amount<0:
        print("*******************")
        print("That is not a valid amount")
    else:
        return amount

def withdraw():
    print("*******************")
    am=float(input("Enter an amount to be withdrawn ₹: "))
    
    if am>balance:
        print("Insufficient funds")
        return 0
    elif am<0:
        print("*******************")
        print("Amount must be greater than 0")
        return 0
    else:
        return am

balance=0;
is_running=True

while is_running:
    print("*******************")
    print("*******************")
    print("Bank management system")
    print("*******************")
    print("1.Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4.Exit")
    print("*******************")
    
    choice=int(input("Enter your choice(1-4): "))
    
    if choice==1:
        show_balance()
    elif choice==2:
        balance+=deposit()
    elif choice==3:
        balance-=withdraw()
    elif choice==4:
        is_running=False
    else:
        print("*******************")
        print("That is not a valid choice")

print("*******************")
print("Thank you! Have a nice day!")
print("*******************")