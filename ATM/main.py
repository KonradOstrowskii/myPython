from account import accesAccount, Menu
a = accesAccount()
m = Menu()
choice = 0
while True:
    choice = input("Your next step :")
    if choice == "1":
        m.bilans()
        continue
    elif choice == "2":
        m.deposit()
    elif choice == "3":
        m.try_withdraw()
    elif choice == "4":
        m.exit()
        quit()
