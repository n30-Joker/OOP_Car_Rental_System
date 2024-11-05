from customer import Customer, VIP
from cars import Hatchback, Sedan, SUV


class RentalShop:
    """
    A class to represent a car rental shop.

    Attributes:
        name (str): The name of the shop.
        car_types (dict): A dictionary which maps car type names to their
            respective objects.
        stock (dict): A dictionary mapping car type names to a list of available
            cars in the rental shop garage.
        vip_list (list): A list of customers' names who are signed up to the shop's
            loyalty programme.
    """

    def __init__(self, name):
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
            name (str): The rental shop's name.
        """
        self.name = name
        self.car_types = {
            "Hatchback": Hatchback(),
            "Sedan": Sedan(),
            "SUV": SUV()
            } # Currently only three types of cars are sold on this platform.
        self.stock = {
            "Hatchback":[],
            "Sedan":[],
            "SUV":[]
            } # The stock is initially empty.
        self.vip_list = [
            "Customer1(VIP)", 
            "Customer2(VIP)", 
            "Customer3(VIP)"
            ] # Assume 3 VIP customers exist.

    def get_name(self):
        return self.name
    
    # Private method to add a car to the stock.
    def __add_car(self, key, car):
        """
        Adds a car to the stock for a specific car type.
        
        Parameters:
            key (str): The car type.
            car: Thr car object to add to the list.
        """
        self.stock[key].append(car)

    def return_car(self, key, car):
        """
        Adds a returned car back to the stock.

        Parameters:
            key (str): The type of car being returned.
            car: The car object being returned.

        Returns:
            bool: True if the car was successfully added back,
                False if the car type does not exist.
        """
        try:
            self.__add_car(key, car)
            return True
        except KeyError: # Handles the error of the car type not existing.
            return False

    def add_to_stock(self, key, amount):
        """
        Adds a specified number of cars to the stock for a specific
        car type.

        Parameters:
            key (str): The type of car to add to stock.
            amount (int): The number of cars to add to the garage.
        """
        for i in range(amount):
            self.__add_car(key, self.car_types[key])

    def get_stock(self):
        """
        Displays a summary of the stock for each type of car, including
        the total stock count.
        """
        sum = 0
        stock_summary = "| "

        # Iterate through the stock dictionary to build the stock summary text.
        for key in self.stock:
            amount = len(self.stock[key])
            stock_summary += key + ": " + str(amount) + " | "
            sum += amount
        
        print(
            "\n################STOCK################\n"
            + stock_summary 
            + f"\nTotal: {sum}"
            "#####################################"
            )

    def give_the_car(self, key):
        """
        Removes and returns a car from stock of the specified type.

        Assumptions:
            Following the LIFO (Last-In First-Out) approach, the last
            car added to the stock will be the first one to be rented.
            This is carried out for simplicity.

        Parameters:
            key (str): The type of car to rent out.

        Returns:
            The car object that was rented out.
        """
        return self.stock[key].pop() # Returns the last car from the list (LIFO).
    
    def available(self, key):
        """
        Checks if there are any cars available in the garage for the specific
        car type.

        Parameters:
            key (str): The type of car to check availability for.

        Returns:
            bool: True if the car type is in stock, otherwise False.
        """
        try:
            return len(self.stock[key]) > 0
        except KeyError: # Type of car is not sold in this shop.
            return False
    
    def get_rate(self, car, num_days, is_vip):
        """
        Retrieves the rate for renting a car based on the rental duration
        and the VIP status of the customer.

        Parameters
        """
        if is_vip:
            return car.get_vip_rate()
        
        if num_days < 7:
            return car.get_below_week_rate()
        else:
            return car.get_week_or_more_rate()    

    def get_price(self, rate, num_days):
        return rate * num_days   

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

