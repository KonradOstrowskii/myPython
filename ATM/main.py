from account import accesAccount, Menu
a = accesAccount()
m = Menu()
choice = 0
while True:
    choice = input("Your next step :")
    if choice == "1":
        m.bilans()
        continue
    if choice == "2":
        m.deposit()
    if choice == "3":
        m.try_withdraw()
    if choice == "4":
        m.exit()
        quit()
