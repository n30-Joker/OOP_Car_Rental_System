from customer import Customer, VIP
from cars import Hatchback, Sedan, SUV

class RentalShop:

    def __init__(self, name):
        self.name = name
        self.car_types = {
            "Hatchback": Hatchback(),
            "Sedan": Sedan(),
            "SUV": SUV()
            } 
        self.stock = {
            "Hatchback":[],
            "Sedan":[],
            "SUV":[]
            }
        self.vip_list = ["Customer1(VIP)", "Customer2(VIP)", "Customer3(VIP)"]

    def get_name(self):
        return self.name
    
    # Private method
    def __add_car(self, key, car):
        self.stock[key].append(car)

    def return_car(self, key, car):
        try:
            self.__add_car(key, car)
            return True
        except KeyError:
            return False

    def add_to_stock(self, key, amount):
        for i in range(amount):
            self.__add_car(key, self.car_types[key])

    def get_stock(self):
        sum = 0
        text = "| "

        for key in self.stock:
            amount = len(self.stock[key])
            sum += amount
            text += key + ": " + str(amount) + " | "
        
        print(
            "\n################STOCK################\n"
            + text 
            + f"\nTotal: {sum}"
            "#####################################"
            )

    def give_the_car(self, key):
        return self.stock[key].pop()
    
    def available(self, key):
        try:
            if len(self.stock[key]) > 0:
                return True
            else:
                return False
        except KeyError:
            return False
    
    def get_rate(self, car, days, is_vip):
        if is_vip:
            return car.get_vip_rate()
        
        if days < 7:
            return car.get_below_week_rate()
        else:
            return car.get_week_or_more_rate()    

    def get_price(self, rate, days):
        return rate * days   

    def upgrade(self, client):
        print("You have now joined our loyalty programme!")
        name = client.get_name() + "(VIP)" # Add VIP tag.
        vip_client = VIP(name)
        vip_client.transfer_details(client)
        self.vip_list.append(name)
        return vip_client    

    def downgrade(self, vip_client):
        print("We are sorry to have you leave our loyalty programme...")
        name = vip_client.get_name()
        client = Customer(name[:-5]) # Remove VIP tag.
        client.transfer_details(vip_client)
        self.vip_list.remove(name)
        return client

