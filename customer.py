class Customer:
    """
    Represents a customer who can rent cars, 
    with attributes to track rental details.

    Assumption:
        Only one car can be rented per customer.

    Attributes:
        name (str): The name of the customer.
        car_details (dict): Dictionary holding 
            details about the current car rental.
    """
    
    def __init__(self, name):
        """
        Initialises a Customer instance with the customer's name
        and car details.

        Assumption:
            A new customer does not hold any car.

        Parameters:
            name (str): Customer name.
        """
        self.name = name
        self.car_details = {} # Stores details of the car the customer has rented.
        self.no_car() # Initialises the dictionary with no data. The new customer has no cars.
    
    def no_car(self):
        """
        Resets the customer's car details to have no cars.
        """
        self.car_details = {
            "car": None,    # No car rented.
            "type": None,   # No car type specified.
            "days": 0       # Zero days rented.
            }

    def get_name(self):
        return self.name

    def get_car_cetails(self):
        return self.car_details
    
    def set_car_cetails(self, car_details):
        """
        Updates the car details for the customer.

        Parameters:
            car_details (dict): Holds updated details.
        """
        self.car_details = car_details

    def car_rented(self):
        """
        Checks if the customer currently holds a rented car.

        Returns:
            bool: True if a car is rented, False otherwise.
        """
        return self.car_details["car"] is not None # None implies the customer has no car.
        
    def rent_car(self, car_obj, car_type, num_days):
        """
        Transfer car rental details for the customer from the shop.

        Parameters:
            car_obj: The car object being rented.
            car_type (str): The type of the car (e.g. Hatchback, Sedan or SUV).
            num_days (str): The number of days the car is rented for.
        """
        self.car_details["car"] = car_obj
        self.car_details["type"] = car_type
        self.car_details["days"] = num_days

    def return_car(self):
        """
        Empties the customer's garage and returns the car details.

        Returns:
            car_returned (dict): Contains details of the returned car.
        """
        car_returned = {
            "car": self.car_details.pop("car"),
            "type": self.car_details.pop("type"),
            "days": self.car_details.pop("days")
            } # Capture the details to return in a dictionary.
        self.no_car() # Reset inventory with no car.
        return car_returned # Returns the details of the returned car.
    
    def vip_status(self):
        """
        Specifies if the customer has a loyalty programme.

        Defaults:
            Standard customers have no VIP status.

        Returns:
            bool: False, as the customer is not a VIP.
        """
        return False
    
    def transfer_details(self, client):
        """
        Transfers car rental details from one account to another.

        Parameters:
            client (Customer): Account whose details are to be copied.
        """
        self.set_car_cetails(client.get_car_cetails())


class VIP(Customer):
    """
    VIP customer class, enabling the customer to access discounted rates.

    Inherits methods from the Customer class, and specifies the customer's name.

    Overrides the vip_status to reflect the customer's status.
    """

    def __init__(self, name): # Can add more paramters later.
        """
        Initialises a VIP instance with the provided name.

        Parameters:
            name (str): Name of the customer with the loyalty programme.
                The naming convention is 'customer_name(VIP)'.
        """
        super().__init__(name)
    
    def vip_status(self):
        """
        Returns the VIP status of the customer.

        Returns:
            bool: True, stating the customer is a loyalty programme member. 
        """
        return True