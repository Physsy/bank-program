def deposit():
    amount=float(input("Enter amount to deposit: "))
    if amount < 0:
        print(f"{amount} not a valid amount")
    else:
        return amount
def withdraw():
    amt = float(input("how much are you withdrawimg: "))
    if amt > bal:
        print(f"insufficient balance to draw{amt}")
    else:
        print(f"{amt} withdrawn")
        return amt   
def balance():
    print(f"your balance is €{bal:.2f}")
    
def exit():
    print("have a nice day")
    
 
bal = 0
bank = True
while bank:
    print("bank(ATM)")
    print("1.deposit \n"
          "2.balance \n"
          "3.withdraw \n"
          "4.exit")
    choice = input("enter your choice (1-4): ")
    if choice == '1':
        bal += deposit()
    elif choice == '2':
        balance()
    elif choice == '3':
        bal -= withdraw()
    elif choice == '4':
        exit() 
        bank = False