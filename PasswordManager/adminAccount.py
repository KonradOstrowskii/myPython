
class Message:
    def __init__(self ,successMessage,failMessage):
        self.successMessage = successMessage
        self.failMessage = failMessage


class Admin(Message):
    def __init__(self):
        count = 0
        key_pwd = "master"
        while True:
            if count > 3:
                print("Error")
                quit()

            master_pwd = input('Please enter Your Admin password: ')
            if master_pwd == key_pwd:
                print("OKi")
                break
            else:
                print('Access denied. Try again.')
                count += 1
                if count >= 3:
                    print("invalid password , account is blocked")
                    print("Contact with your Our Support")
                    quit()