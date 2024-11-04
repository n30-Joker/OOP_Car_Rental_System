class Customer:

    def __init__(self, name):
        self.name = name
        self.carDetails = {}
        self.noCar()
    
    def noCar(self):
        self.carDetails = {
            "car": None,
            "type": None,
            "days": 0
        }

    def getName(self):
        return self.name

    def getCarDetails(self):
        return self.carDetails

    def carRented(self):
        if self.carDetails["car"] != None:
            return True
        else:
            return False
        
    def rentCar(self, carObj, carType, numDays):
        self.carDetails["car"] = carObj
        self.carDetails["type"] = carType
        self.carDetails["days"] = numDays

    def returnCar(self):
        carReturned = { "car": self.carDetails.pop("car"),
            "type": self.carDetails.pop("type"),
            "days": self.carDetails.pop("days")}
        self.noCar()
        return carReturned
    
    def VIPStatus(self):
        return False
    
    def transferDetails(self, client):
        self.carDetails = client.getCarDetails()
    
class VIP(Customer):
    def __init__(self,name):
        super().__init__(name)
    
    def VIPStatus(self):
        return True