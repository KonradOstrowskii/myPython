
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
        try:
            amount = int(input("Enter amount to be Deposited: "))
            self.balance += amount
            print(True, "Amount Deposited:", amount)
            print("Your balance is : ", self.balance, "$")
            self.printMenu()
        except Exception as e:
            print("Sorry there was and Issue with Details:\n{}  ".format(e))
            print("Put only  int digits here")
        finally:
            print("Please, Try Again")

    def try_withdraw(self):
        try:
            amount = int(input("Enter amount to be Withdrawn: "))
            if (self.balance >= amount):
                self.balance - amount
                print("You Withdrew: ", amount)
                return True
        except Exception as e:
            print("Sorry there was and Issue with {}  ".format(e))
            print("Put only digits here")
            print("Insufficient balance  ", self.balance)
            return False
        finally:
            print("Please, Try Again")

    def bilans(self, balance=1000):
        print("You balance is : ", self.balance)
        self.printMenu()

    def exit(self):
        print("Thank You ,Have a nice day")
