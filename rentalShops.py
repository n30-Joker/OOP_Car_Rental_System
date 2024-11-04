from customer import Customer, VIP
from cars import Hatchback, Sedan, SUV

class RentalShop:

    def __init__(self, name):
        self.name = name
        self.carTypes = {
            "Hatchback": Hatchback(),
            "Sedan": Sedan(),
            "SUV": SUV()
        } 
        self.stock = {
            "Hatchback":[],
            "Sedan":[],
            "SUV":[]
        }
        self.VIPList = ["VIP1", "VIP2", "VIP3"]

    def getName(self):
        return self.name

    def getKeys(self):
        return self.stock.keys()
    
    def getValues(self):
        return self.stock.values()
    
    def getItems(self):
        return self.stock.items()
    
    # Private method
    def __addCar(self, key, car):
        self.stock[key].append(car)

    def returnCar(self, key, car):
        try:
            self.__addCar(key, car)
            return True
        except KeyError:
            return False

    def addToStock(self, key, amount):
        for i in range(amount):
            self.__addCar(key, self.carTypes[key])

    def getStock(self):
        sum = 0
        text = "| "

        for key in self.stock:
            amount = len(self.stock[key])
            sum += amount
            text += key + ": " + str(amount) + " | "
        
        print("\n################STOCK################")
        print(text + f"\nTotal: {sum}")
        print("#####################################")

    def removeStock(self, key):
        return self.stock[key].pop()
    
    def available(self, key):
        try:
            if len(self.stock[key]) > 0:
                return True
            else:
                return False
        except KeyError:
            return False
    
    def getRate(self, car, days, isVIP):
        if isVIP:
            return car.getVIPRate()
        if days < 7:
            return car.getBelowWeekRate()
        else:
            return car.getWeekOrMoreRate()
    
    def getVIPRate(self, car):
        return car.getVIPRate()    

    def getPrice(self, rate, days):
        return rate * days   

    def upgrade(self, client):
        print("You have now joined our loyalty programme!")
        name = client.getName() + "(VIP)"
        VIPClient = VIP(name)
        VIPClient.transferDetails(client)
        self.VIPList.append(name)
        return VIPClient    

    def downgrade(self, VIPClient):
        print("We are sorry to have you leave our loyalty programme...")
        name = VIPClient.getName()
        client = Customer(name[:-5])
        client.transferDetails(VIPClient)
        self.VIPList.remove(name)
        return client

