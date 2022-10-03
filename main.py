class Wallet:
    def __init__(self, money=0):
        self.money = money
          
    def __str__(self):
        return f"This wallet has  {self.money}"

    def credit(self,amount):
        self.money += amount
        print(f"you have : {self.money}")
        


    def debit(self,amount):
        self.money -= amount
        print(f"you have : {self.money}")
        


wallet = Wallet(6)
 
 

class Person:
    def __init__(self, name, location,money ):
        self.name= name
        self.location= location
        self.wallet= Wallet(money)

    def moveTo(self, point):
         self.location = point
    
person = Person("Moh ", 5, 50)   

class Vendor(Person):
#     # implement Vendor!

    def __init__(self, name, location,money):
        super().__init__(name,location,money)
        self.range = 5
        self.price = 1
        

    def sellTo(self,customer,number_of_icecream):
        self.location = customer.location
        self.wallet.credit(number_of_icecream*self.price)
        customer.wallet.debit(self.price * number_of_icecream)
        print(f"{number_of_icecream} were sold")

    def __str__(self):
        return f"your range is {self.range} and the remaining price is {self.price}KWD"

        

class Customer(Person):
#     # implement Customer!
    def __init__(self, name, location,money ):
        super().__init__(name,location,money)

    def _is_in_range(self, vendor):
        distance= vendor.location -self.location
        if distance>vendor.range:
            print("yeey!! you are in range")
            return True

        else:
            print("sorry you are out of range")
            return False

    def _have_enough_money(self, vendor, number_of_icecreams):
        
        if self.wallet.money >= (vendor.price * number_of_icecreams):
            print("you have enough money")
            return True 
        else:
            print("you dont have enough money")
            return False 
    
    def request_icecream(self, vendor, number_of_icecreams):
        
        if self._is_in_range(vendor) and self._have_enough_money(vendor,number_of_icecreams):
            print("request has been made")
            vendor.sellTo(self,number_of_icecreams)
        
    def __str__(self):
        return f"you are the customer{super().__str__()}"
        

    
vendor_Anfal = Vendor("Anfal", 10, 10 )
nearby_customer = Customer("Ali",12, 10)
distant_customer = Customer("Adal",1000,500)
nearby_customer.request_icecream(vendor_Anfal,10)
print(nearby_customer.wallet.money)
print(vendor_Anfal.wallet.money)
print(vendor_Anfal.location)

