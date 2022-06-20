from Menu import Menu
from Stock import Stock

class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.LogedIn = False
        self.discount = False
        self.count= 0
        

    def login(self):
        
        self.count = 0
        while True:
            with open("UserRegister.txt", "r", encoding='utf-8') as file:
                
                self.username = input("Enter username: ")
                self.password = input("Enter password: ")
                if self.count > 3:
                    self.username = input("Enter username: ")
                    self.password = input("Enter password: ")
                    
                    
                if self.username and self.password in file.readline():
                    print("login successful!")
                    
                    break
                            
                if self.count >=3:
                        print("login failed!")
                        self.count = 0
                        break
                    
    def register(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        self.pass_check = input("Confirm password: ")
        self.email = input("Enter email: ")
        with open("UserRegister.txt", "a+", encoding='utf-8') as file:
                file.write('Username:'+ self.username +' '+ 'Password:'+
                    self.password+' '+ 'email:'+ self.email + '\n')                    
class AdminUser(Stock):
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
    def register(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")
        self.pass_check = input("Confirm password: ")
        self.email = input("Enter email: ")
        with open("UserRegister.txt", "a+", encoding='utf-8') as file:
                file.write('Username:'+ self.username +' '+ 'Password:'+
                           self.password+' '+ 'email:'+ self.email + '\n')
    
            
    def decrement_stock_by_admin(self,x):
        x = int(input("Enter the value to decrement: "))
        self.stock -= x
        return self.avaible_stock
        
            
        
    def increase_stock_by_admin(self,x):
        x = int(input("Enter the value to increase :"))
        self.stock += x
        return self.avaible_stock


    
