class User():
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def login(self, username, password):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        

    def register(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        self.pass_check = input("Enter password: ")
        self.email = input("Enter email: ")
        
x = User.register(User)

print(x.__init__)

    
