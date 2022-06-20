
from User import  *
from Stock import Stock
from Menu import Menu,AdminMenu


def calculate_value_vat_cart(x : float):
    y = float(x) * 0.23
    return round(y,2)
        
        
              
hdmi = Stock("hdmi",45,15)
vga = Stock("vga",20,50)
jack = Stock("jack",40,40)    
 
           

                         

choice = 0

shopping_cart = []
cart_value = 0 

while True:  
        Menu.menu(Menu)
        choice = input("Your next step :")
        if choice =="1":
            print(hdmi.avaible_stock())
            print(hdmi.vat_calculate())
            print(vga.avaible_stock())
            print(vga.vat_calculate())
            print(jack.avaible_stock())
            print(jack.vat_calculate()) 
            
        if choice =="2":
            print("Your shopping cart contains",shopping_cart," value is",cart_value," PLN , the tax is",calculate_value_vat_cart(cart_value),"PLN")        
            
        if choice == "3":
                while True:
                    print(hdmi.avaible_stock())
                    print(vga.avaible_stock())
                    print(jack.avaible_stock())
                    x = input("Enter items from inventory wich You would like to select(hdmi,vga,jack,q for quit) :").lower()
                    if x == "hdmi":
                        shopping_cart.append("HDMI")
                        cart_value += 45
                        hdmi.avaible_stock()
                        hdmi.decrement_stock()
                    elif x == "vga":
                        shopping_cart.append("VGA")
                        cart_value += 20
                        vga.decrement_stock()
                    elif x == "jack":
                        shopping_cart.append("JACK")
                        cart_value += 40
                        jack.decrement_stock()
                    elif x == "q":
                        break
                
        if choice == "4":
            print("You shopping_cart",shopping_cart)
            o = input("Would you like to remove [hdmi,vga,jack] from your inventory?q for back to the main menu :")
            if o == "hdmi":
                hdmi.stock += 1
                shopping_cart.remove('HDMI')
                cart_value -= 45
            if o == "vga": 
                vga.stock += 1
                shopping_cart.remove('VGA')
                cart_value -= 20
            if o == "jack":
                jack.stock += 1
                shopping_cart.remove('JACK')
                cart_value -= 40
                
                    
                
            if o == "q":
                Menu()
        
        if choice == "5":   
            
            accuount=input("Would you like to create a new account (y) or log into Your account(l)?(q)for back to main menu : ") 
            if accuount == "l":
                User.login(User)
               
            elif accuount == "y":
                User.register(User)
                Menu.menu(Menu)
            elif accuount == "q":
                Menu.menu(Menu)
        
        if choice == "7":
            AdminMenu.admin_menu(AdminMenu)
            chose = input("Enter your choice: ")
            if chose == "1":
                pass
            if chose == "2":   
                pass
            if chose == "3":   
                x = int(input("what item You want to decrement 1.HDMI 2.VGA 3.JACK :"))
                if x == 1:
                    x = int(input("Enter the value to decrement: "))
                    AdminUser.decrement_stock_by_admin(hdmi,x)
                    Menu.menu(Menu)
                if x == 2: 
                    x = int(input("Enter the value to decrement: "))
                    AdminUser.decrement_stock_by_admin(vga,x)
                    Menu.menu(Menu) 
                if x == 3:
                    x = int(input("Enter the value to decrement: "))
                    AdminUser.decrement_stock_by_admin(jack,x)
                    Menu.menu(Menu)
            if chose == "4":
                x = int(input("what item You want to decrement 1.HDMI 2.VGA 3.JACK :"))
                if x == 1:
                    x = int(input("Enter the value to decrement: "))
                    AdminUser.increase_stock_by_admin(hdmi,x)
                    Menu.menu(Menu)
                if x == 2:
                    x = int(input("Enter the value to decrement: "))
                    AdminUser.increase_stock_by_admin(vga,x)
                    Menu.menu(Menu)
                if x == 3:
                    x = int(input("Enter the value to decrement: "))
                    AdminUser.increase_stock_by_admin(jack,x)
                    Menu.menu(Menu)
                        
        if choice == "6":
            print("GoodBye see you!")
            break
