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
        self.wallet=Wallet(money)
    
    def moveTo(point):
        point = Person(location)
        print(self.point)




# person = Person("Moh", 5, 50)


class Vendor:
#     # implement Vendor!
#     pass
    def __init__(self, name, location,money ):
        super().__init__(name,location,money)
        self.range = 5
        self.price = 1
    def sellTo(customer,number_of_icecream):
        self.customer = customer
        self.number_of_icecream = number_of_icecream
        while range<5 and price>0:
            print("their is only 3 icecream")
# vendor = Vendor("Abdallah", 3, 6)


# class Customer:
#     # implement Customer!
#     pass


# customer = Customer("Abdallah", 3, 6)
