class Stock:
    def __init__(self,name : str,current_price : float ,stock : int):
        """
        :param name: Name of a product 
        :param stock: Current quantity
        :param current_price: Current price of  the product 
        """
        self.current_price = current_price
        self.stock = stock
        self.name = name
        
        with open("Stock.txt", "a", encoding='utf-8') as file:
                file.write('Name:'+ self.name +' '+ 'stock: '+
                           str(self.stock)+' '+ 'current_price: '+ str(self.current_price))
        
    def avaible_stock(self):
        return (f"Current number of cables {self.name} is {self.stock}")
        
    def price(self):
        print(f"{self.name} cable is {self.current_price}PLN")
        
        
    def vat_calculate(self):
        vat = self.current_price * 0.23
        return (f'Coast of {self.name} cable is {self.current_price} PLN while VAT is 23% wich is' ,round(vat,2) ,"PLN")
    
    def decrement_stock(self):
        self.stock -= 1
        return self.avaible_stock
  