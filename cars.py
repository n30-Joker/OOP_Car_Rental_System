class Car:
    def __init__(self, belowWeek, weekOrMore, VIP):
        self.belowWeek = belowWeek
        self.weekOrMore = weekOrMore
        self.VIP = VIP

    def getBelowWeekRate(self):
        return self.belowWeek
    
    def getWeekOrMoreRate(self):
        return self.weekOrMore
    
    def getVIPRate(self):
        return self.VIP
    
class Hatchback(Car):
    def __init__(self):
        super().__init__(30, 25, 20)

class Sedan(Car):
    def __init__(self):
        super().__init__(50, 40, 35)

class SUV(Car):
    def __init__(self):
        super().__init__(100, 90, 80)