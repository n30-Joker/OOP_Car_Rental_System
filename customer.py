# Customer and VIP classes holding the client's information.
class Customer:
    """
    Represents a customer who can rent cars, 
    with attributes to track rental details.

    Assumption:
        Only one car can be rented per customer.

    Attributes:
        customer_name (str): The name of the customer.
        car_details (dict): Dictionary holding 
            details about the current car rental.
    """
    
    def __init__(self, customer_name):
        """
        Initialises a Customer instance with the customer's name
        and car details.

        Assumption:
            The customer only has a name, for simplicity.
            A new customer does not hold any car.

        Parameters:
            customer_name (str): Customer name.
        """
        self.customer_name = customer_name # Can add other details, e.g. email, age, gender.
        self.car_details = {} # Stores details of the car the customer has rented.
        self.__empty_garage() # Initialises the dictionary with no data. The new customer has no cars.
    
    # Private method, works only within the class.
    def __empty_garage(self):
        """
        Resets the customer's car details to have no cars.
        """
        self.car_details = {
            "car": None,    # No car rented.
            "type": None,   # No car type specified.
            "days rented": 0       # Zero days rented.
            }

    def get_customer_name(self):
        return self.customer_name

    def get_car_details(self):
        return self.car_details
    
    def set_car_details(self, car_details):
        """
        Updates the car details for the customer.

        Parameters:
            car_details (dict): Holds updated details.
        """
        self.car_details = car_details

    def is_renting_a_car(self):
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
            num_days (int): The number of days the car is rented for.
        """
        self.car_details["car"] = car_obj
        self.car_details["type"] = car_type
        self.car_details["days rented"] = num_days

    def return_car(self):
        """
        Empties the customer's garage and returns the car details.

        Returns:
            returned_car_details (dict): Contains details of the returned car.
        """
        returned_car_details = {
            "car": self.car_details.pop("car"),
            "type": self.car_details.pop("type"),
            "days rented": self.car_details.pop("days rented")
            } # Capture the details to return in a dictionary.
        self.__empty_garage() # Reset inventory with no car.
        return returned_car_details # Returns the details of the returned car.
    
    def is_vip(self):
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
        self.set_car_details(client.get_car_details())


class VIP(Customer):
    """
    VIP customer class, enabling the customer to access discounted rates.

    Inherits methods from the Customer class, and specifies the customer's name.

    Overrides the is_vip method to reflect the customer's status (polymorphism).
    """

    def __init__(self, vip_name): # Can add more paramaters later.
        """
        Initialises a VIP instance with the provided name.

        Parameters:
            vip_name (str): Name of the customer with the loyalty programme.
                The naming convention is 'customer_name(VIP)'.
        """
        super().__init__(vip_name)
    
    def is_vip(self):
        """
        Returns the VIP status of the customer.

        Returns:
            bool: True, stating the customer is a loyalty programme member. 
        """
        return True