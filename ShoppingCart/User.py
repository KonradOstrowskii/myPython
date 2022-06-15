class User():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def login(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        with open("UserRegister.txt", "r", encoding='utf-8') as file:
            if "Username: " in file   == self.username and "Password: " in file == self.password:
                print("login successful!")
            else:
                print("wrong password entered")

            if self.username == self.username and self.password == self.password:
                print("login successful!")

        

    def register(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        self.pass_check = input("Confirm password: ")
        self.email = input("Enter email: ")
        with open("UserRegister.txt", "a", encoding='utf-8') as file:
                file.write('Username:'+ self.username +' '+ 'Password:'+
                           self.password+' '+ 'email:'+ self.email)
    
