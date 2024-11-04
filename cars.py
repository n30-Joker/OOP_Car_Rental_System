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
    """
    Hatchback car class with predefined daily rates.

    Inherits all the methods from the Car class and sets 
    specific daily rates.
    """
    def __init__(self):
        """
        Initialises a Hatchback instance with the following rates:
            - less than 7 days at £30 per day;
            - 7 days or more at £25 per day;
            - a special rate of £20 per day for VIP customers.
        """
        super().__init__(30, 25, 20)

class Sedan(Car):
    """
    Sedan car class with predefined rates.

    Inherits methods from Car class and specifies
    the daily rates.
    """
    def __init__(self):
        """
        Initialises a Sedan instance with the following rates:
            - less than 7 days at £50 per day;
            - 7 days or more at £40 per day;
            - a special rate of £35 per day for VIP customers.
        """
        super().__init__(50, 40, 35)

class SUV(Car):
    """
    SUV car class with determined daily rates.

    Inherits methods from Car class and states
    the daily rates.
    """
    def __init__(self):
        """
        Initialises a SUV instance with the following rates:
            - less than 7 days at £100 per day;
            - 7 days or more at £90 per day;
            - a special rate of £80 per day for VIP customers.
        """
        super().__init__(100, 90, 80)