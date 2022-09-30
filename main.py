class Wallet:
    def __init__(self, money):
        self.money = money
          


    def credit(self,amount):
        self.money += amount
        print(f"you have : {self.money}")
        


    def debit(self,amount):
        self.money -= amount
        print(f"you have : {self.money}")
        


# wallet = Wallet(6)
# wallet = Wallet()  # This should default money inside the wallet to 0
# print(wallet.money)
# wallet.credit(2)


class Person:
    def __init__(self, name, location,money ):
        self.name= name
        self.location= location
        self.money= Wallet(money)

    def moveTo(self, point):
         point = Person(location)
         print(self.point)

class Vendor(Person):
#     # implement Vendor!

    def __init__(self, name, location,money,range,price):
        super().__init__(name,location,money)
        self.range = range
        self.price = price
        range = 5
        price = 1

    def sellTo(self,customer,number_of_icecream):
        self.customer = customer
        self.number_of_icecream = number_of_icecream
        self.moveTo(customer.location)
        self.wallet.credit(self.price * number_of_icecream)
        customer.wallet.debit(self.price * number_of_icecream)
        print(f"{number_of_icecream} were sold")

    def __str__(self):
        return f"your range is {self.range} and the remaining price is {self.price}KWD"

        

class Customer(Person):
#     # implement Customer!
    def __init__(self, name, location,money ):
        super().__init__(name,location,money)
    def _is_in_range(self, vendor):
        self.vendor = vendor
        if abs(location - vendor.location)<= vendor.range:
            print("the customer is in range")
            return true

        else:
            print("the customer is out of range")
            return false
    def _have_enough_money(self, vendor, number_of_icecreams):
        self.vendor = vendor
        self.number_of_icecreams = number_of_icecreams
        if self.wallet.money >= (vendor.price * number_of_icecreams):
            print("you have enough money")
            return True 
        else:
            print("you dont have enough money")
            return False 
    
    def request_icecream(self, vendor, number_of_icecreams):
        self.vendor = vendor
        self.number_of_icecreams = number_of_icecreams
        if self._is_in_range and self._have_enough_money:
            print("request has been made")
            vendor.sellTo(customer,number_of_icecreams)
        
    def __str__(self):
        return f"you are the customer{super().__str__()}"
        

    
vendor = Vendor("Anfal", 3, 6 )
customer = Customer("Ali", 20, 6 )
customer.request_icecream(vendor, 3)