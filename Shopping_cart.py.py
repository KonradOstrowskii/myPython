
class Stock:
    def __init__(self,name : str,current_price : int ,stock : int):
        """
        :param name: Name of a product 
        :param stock: Current quantity
        :param current_price: Current price of  the product 
        """
        self.current_price = current_price
        self.stock = stock
        self.name = name
        
    def avaible_stock(self):
        return (f"Current number of cables {self.name} is {self.stock}")
        
    def price(self):
        print(f"{self.name} cable is {self.current_price}PLN")
        
        
    def vat_calculate(self):
        vat = self.current_price * 0.23
        return (f'Coast of {self.name} cable is {self.current_price} PLN while VAT is 23% wich is' ,round(vat,2) ,"PLN")
    
    def calculate_stock(self):
        self.stock -= 1
        return self.avaible_stock
    
    
      
    

def calculate_value_vat_cart(x : float):
    y = float(x) * 0.23
    return round(y,2)
        
        
              
hdmi = Stock("hdmi",45,15)
vga = Stock("vga",20,50)
jack = Stock("jack",40,40)    
 
           
class Menu:
    
    def __init__(self):
        print("""
                Menu: 
                    1.Check all avaible items
                    2.Shopping Cart
                    3.Add Items
                    4.Remove Items/Clear Cart
                    5.Exit
                    What's Your next step :""")
                         

choice = 0

shopping_cart = []
cart_value = 0 
while True:  
        
    Menu()
    choice = input("Your next step :")
    if choice =="1":
        print(hdmi.avaible_stock())
        print(hdmi.vat_calculate())
        print(vga.avaible_stock())
        print(vga.vat_calculate())
        print(jack.avaible_stock())
        print(jack.vat_calculate()) 
    
    if choice =="2":
        print("Your shopping_cart contains",shopping_cart," value is",cart_value," PLN , the tax is",calculate_value_vat_cart(cart_value),"PLN")        
    
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
                hdmi.calculate_stock()
            elif x == "vga":
                shopping_cart.append("VGA")
                cart_value += 20
                vga.calculate_stock()
            elif x == "jack":
                shopping_cart.append("JACK")
                cart_value += 40
                jack.calculate_stock()
            elif x == "q":
                break
           
    if choice == "4":
        print("You shopping_cart",shopping_cart)
        o = input("Would you like to remove [hdmi,vga,jack] from your inventory?")
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
            
        
        if o == "n":
            Menu()
       
            
    if choice == "5":
        print("GoodBye see you!")
        break