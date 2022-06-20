
from User import *
from Stock import Stock




class Menu:
      
    def menu(self):
        print("""
                Menu: 
                    1.Check all avaible items
                    2.Shopping Cart
                    3.Add Items
                    4.Remove Items
                    5.Login
                    6.Exit
                    What's Your next step :""")
        
        
class AdminMenu(Stock):  
    def admin_menu(self):
        print(""""
              1.remove user
              2.add user
              3.decrement stock
              4.increase stock
              """)
        
            