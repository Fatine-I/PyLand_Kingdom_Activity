#The Royal Bank
balance=1000
def deposit(balance):
    print("How much?\n")
    d=int(input(" "))
    n_balance=balance+d
    print(f"Deposited {d}\n new balance: {n_balance}")
    balance=n_balance
def withdraw(balance):
    print("How much?\n")
    w=int(input(" "))
    if w>balance:
        print("Sorry! Cannot withdraw more that the balance.")
    else:    
        n_balance=balance-w
        print(f"Withdrew {w}\n new balance: {n_balance}")
        balance=n_balance
def check_balance(balance):    
    print(f"Current balance: {balance}")
print("Hi, what would like to do?\n")
print("1.Deposit\n2.Withdraw\n3.Check balance")
try:
    option=int(input("Option: "))
    if not option in (1,2,3):
        raise ValueError("Only 1, 2 and 3 options are available")
except (TypeError, ValueError) as e:
    print(e)

if option==1:
    deposit(balance)
elif option==2:
    withdraw(balance)
elif option==3:
    check_balance(balance)            