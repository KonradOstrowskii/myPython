
class accesAccount:
    def __init__(self):
        count = 0
        while True:

            if count > 3:
                print("invalid PIN , card is blocked")
                print("Contact with your Bank")
                quit()

            pin = input('Please enter Your Pin: ')
            if pin == "1234":
                print('Access granted')
                break
            else:
                print('Access denied. Try again.')
                count += 1
                if count >= 3:
                    print("invalid PIN , card is blocked")
                    print("Contact with your Bank")
                    quit()


class Menu:

    def __init__(self, balance=1000, amount=0):
        self.printMenu()
        self.balance = balance
        self.balance += amount
        self.balance - amount

    def printMenu(self):
        print("Menu: ")
        print("1.Check balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")

    def deposit(self):
        amount = int(input("Enter amount to be Deposited: "))
        self.balance += amount
        print(True, "Amount Deposited:", amount)
        print(self.balance)
        self.printMenu()

    def try_withdraw(self):
        amount = int(input("Enter amount to be Withdrawn: "))
        if (self.balance >= amount):
            self.balance - amount
            print("You Withdrew: ", amount)
            return True
        else:
            print("Insufficient balance  ", self.balance)
            return False

    def bilans(self, balance=1000):
        print("You balance is : ", self.balance)
        self.printMenu()

    def exit(self):
        print("Thank You ,Have a nice day")
