# RentalShop class for rental transactions with a customer.
from customer import *
from cars import Hatchback, Sedan, SUV


class RentalShop:
    """
    A class to represent a car rental shop.

    Attributes:
        rental_shop_name (str): The name of the shop.
        available_car_types (dict): A dictionary which maps car type names to their
            respective objects.
        rental_shop_stock (dict): A dictionary mapping car type names to a list of available
            cars in the rental shop garage.
        vip_customers (list): A list of customers' names who are signed up to the shop's
            loyalty programme.
    """

    def __init__(self, rental_shop_name):
        """
        Initialises a RentalShop instance with the shop's name, the car types 
        they sell, empty stock and a predefined list of customers who are members
        of the loyalty programme.

        Assumptions:
            Only three car types are sold in the rental shops: hatchbakcs,
                sedans and SUVs.
            Existing VIPs are named Customer1, Customer2 and Customer3, avoiding
                real names, with the '(VIP)' tag added as the identifier.

        Parameters:
            rental_shop_name (str): The rental shop's name.
        """
        self.rental_shop_name = rental_shop_name
        self.available_car_types = {
            "Hatchback": Hatchback(),
            "Sedan": Sedan(),
            "SUV": SUV()
            } # Currently only three types of cars are sold on this platform.
        self.rental_shop_stock = {
            "Hatchback":[],
            "Sedan":[],
            "SUV":[]
            } # The stock is initially empty.
        self.vip_customers = [
            "Customer1(VIP)", 
            "Customer2(VIP)", 
            "Customer3(VIP)"
            ] # Assume 3 VIP customers exist.

    def get_rental_shop_name(self):
        return self.rental_shop_name
    
    # Private method, working only within the class.
    def __add_car(self, car_type, car):
        """
        Adds a car to the stock for a specific car type.
        
        Parameters:
            car_type (str): The car type.
            car: The car object to add to the list.
        """
        self.rental_shop_stock[car_type].append(car)

    def is_returnable(self, car_type, car):
        """
        Checks if the car can be returned, if possible, adds it
        back to the shop's stock.

        Parameters:
            car_type (str): The type of car being returned.
            car: The car object being returned.

        Returns:
            bool: True if the car was successfully added back,
                False if the car type does not exist.
        """
        try:
            self.__add_car(car_type, car)
            return True # The car can be returned and is successfully added.
        except KeyError: # Handles the error of the car type not existing.
            return False

    def add_to_stock(self, car_type, amount):
        """
        Adds a specified number of cars to the stock for a specific
        car type.

        Parameters:
            car_type (str): The type of car to add to stock.
            amount (int): The number of cars to add to the garage.
        """
        for i in range(amount):
            self.__add_car(car_type, self.available_car_types[car_type])

    def display_stock(self):
        """
        Displays a summary of the stock for each type of car, including
        the total stock count.
        """
        sum_of_cars = 0
        stock_summary = "| "

        # Iterate through the stock dictionary to build the stock summary text.
        for car_type in self.rental_shop_stock:
            amount_of_cars = len(self.rental_shop_stock[car_type])
            stock_summary += car_type + ": " + str(amount_of_cars) + " | "
            sum_of_cars += amount_of_cars
        
        print(
            "\n################STOCK################\n"
            + stock_summary 
            + f"\nTotal: {sum_of_cars}\n"
            "#####################################"
            )

    def handout_car(self, car_type):
        """
        Removes and returns a car from stock of the specified type.

        Assumptions:
            Following the LIFO (Last-In First-Out) approach, the last
            car added to the stock will be the first one to be rented.
            This is carried out for simplicity.

        Parameters:
            car_type (str): The type of car to rent out.

        Returns:
            The car object that was rented out.
        """
        return self.rental_shop_stock[car_type].pop() # Returns the last car from the list (LIFO).
    
    def is_available(self, car_type):
        """
        Checks if there are any cars available in the garage for the specific
        car type.

        Parameters:
            car_type (str): The type of car to check availability for.

        Returns:
            bool: True if the car type is in stock, otherwise False.
        """
        try:
            return len(self.rental_shop_stock[car_type]) > 0 # True if there are 0 or more cars of that type, False otherwise
        except KeyError: # Type of car is not sold in this shop.
            return False
    
    def get_rate(self, car, num_days, is_vip):
        """
        Retrieves the rate for renting a car based on the rental duration
        and the VIP status of the customer.

        Assumptions:
            The rate is kept as an integer value.

        Parameters:
            car: The car object being rented.
            num_days (int): The number of days the car is rented for.
            is_vip (bool): Indicates if the customer is part of the
                loyalty programme.

        Returns:
            int: The rental rate for the customer type and 
                specified duration.
        """
        if is_vip: # Special rate no matter how many days.
            return car.get_vip_rate()
        
        if num_days < 7: # Conditional rate for regular customers.
            return car.get_below_week_rate()
        else:
            return car.get_week_or_more_rate()    

    def get_price(self, rate, num_days):
        """
        Calculates the total price of a rental from the rate 
        and length of time the car is rented for.

        Parameters:
            rate (int): The daily rate for renting the car.
            num_days (int): The number of days the car will or
                is rented for.

        Returns:
            int: The total price of the rental.
        """
        return rate * num_days   

    def upgrade(self, client):
        """
        Signs the customer up to the loyalty programme, 
        adding them to the VIP list.

        Parameters:
            client (Customer): The customer being upgraded to VIP.

        Returns:
            vip_client (VIP): A new VIP object with the customer's details transferred.
        """
        print("You have now joined our loyalty programme!")
        vip_customer_name = client.get_customer_name() + "(VIP)" # Add VIP tag.
        vip_client = VIP(vip_customer_name)
        vip_client.transfer_details(client)
        self.vip_customers.append(vip_customer_name)
        return vip_client    

    def downgrade(self, vip_client):
        """
        Downgrade a VIP customer back to a regular customer status,
        as they have decided to leave the loyalty programme, removing
        the VIP privileges.

        Assumptions:
            All VIP customers have a '(VIP)' tag at the end of their name.

        Parameters:
            vip_client (VIP): The VIP customer being downgraded.

        Returns:
            client (Customer): A new Customer object with the VIP's
                details transferred.
        """
        print(
            "We are sorry to have you leave our loyalty programme...\n"
            "You are welcome to sign up again anytime!"
            )
        vip_customer_name = vip_client.get_customer_name()
        client = Customer(vip_customer_name[:-5]) # Remove VIP tag (last 5 characters).
        client.transfer_details(vip_client)
        self.vip_customers.remove(vip_customer_name)
        return client

