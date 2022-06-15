class Menu:
      
    def menu(self):
        print("""
                Menu: 
                    1.Check all avaible items
                    2.Shopping Cart
                    3.Add Items
                    4.Remove Items
                    5.Exit
                    What's Your next step :""")
            
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
            print("GoodBye see you!")
            exit()
