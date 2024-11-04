class Car:
    """
    Base class representing a car with daily rates 
    for different rental durations.

    Attributes:
        belowWeek (int): Daily rate for rentals taken for less than a week.
        weekOrMore (int): Daily rate for rentals lasting a week or longer.
        VIP (int): Discounted daily rate for customers with a loyalty programme.
    """
    def __init__(self, belowWeek, weekOrMore, VIP):
        """
        Initilaises a Car instance with specific daily rates for different scenarios.

        Args:
            belowWeek (int): Rate for rentals shorter than a week.
            weekOrMore (int): Rate for rentals of a week or more.
            VIP (int): Special, discounted rate for VIP customers.
        """
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