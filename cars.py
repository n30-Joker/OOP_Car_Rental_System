class Car:
    """
    Base class representing a car with daily rates 
    for different rental durations.

    Attributes:
        below_week (int): Daily rate for rentals taken for less than a week.
        week_or_more (int): Daily rate for rentals lasting a week or longer.
        vip (int): Discounted daily rate for customers with a loyalty programme.
    """
    def __init__(self, below_week, week_or_more, vip):
        """
        Initilaises a Car instance with specific daily rates for different scenarios.

        Args:
            below_week (int): Rate for rentals shorter than a week.
            week_or_more (int): Rate for rentals of a week or more.
            vip (int): Special, discounted rate for VIP customers.
        """
        self.below_week = below_week
        self.week_or_more = week_or_more
        self.vip = vip

    def get_below_week_rate(self): 
        return self.below_week
    
    def get_week_or_more_rate(self):
        return self.week_or_more
    
    def get_vip_rate(self):
        return self.vip


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