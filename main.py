# Procedural code for the rental platform.
from customer import Customer
from rental_shops import RentalShop
import time


def load():
    """
    Provides a short pause, simulating the loading of different webpages.
    Enables better user experience (UX), as information is not 
    loaded suddenly.
    """
    for i in range(3):
        time.sleep(0.5)
        print(".")
    time.sleep(0.5)


def expected_int(answer):
    """
    Validates the user input to ensure it can be converted
    to an integer. If the input is not an integer, it requests
    the user to re-enter a valid number.

    Assumptions:
        The user eventually enters a whole number (integer).

    Parameters:
        answer (str): The user's input which is expected to be
            an integer.

    Returns:
        answer (int): A valid integer input from the user.
    """
    correct = False
    while not correct:
        try:
            answer = int(answer) # Attempt to convert input to an integer.
        except ValueError:
            # Failed conversion prompts the user to enter a valid number.
            answer = input(
                "You should enter a number, try again.\n\n"
                "Your choice: "
                )
        else:
            correct = True # Exit the loop.
    
    return answer


def go_back():
    """
    Pauses the program until the user presses the enter key to proceed.
    Useful for providing the user with time to read messages.

    Assumptions:
        The user eventually presses the enter key, as all other keys
        lead to nothing.
    """
    input("\n(Press ENTER key to go back.)")
    load()


# Create a new rental shop named 'RentACar'.
# Assumption: For simplicity, only one shop exists in this platform.
shop = RentalShop("RentACar")
# Add cars to the shop's inventory.
# Currently only 3 types of cars available: hatchback, sedan and SUV
shop.add_to_stock("Hatchback", 4)
shop.add_to_stock("Sedan", 3)
shop.add_to_stock("SUV", 3) # Can add more car types later on.

shop.open_shop()
load() # Short pause for better user experience.

# Simple login by entering just a name.
# Assumption: For simplicity, the user does not require any further information 
#   in order to log in to the rental platform.
client_name = input("You are not logged in.\n"
                    "Please enter your name: "
                    )
# Assumption: Customer is initially a regular customer who has not
#   signed up to the loyalty programme.
client = Customer(client_name) # Instantiate a new regular customer with the provided name.
load()

# Main program loop.
while shop.is_currently_open():
    option = input(
        f"{client.get_customer_name()}, what would you like to do?\n"
        "1) Rent a car.\n"
        "2) Check available cars.\n"
        "3) Return car.\n"
        "4) Loyalty programme.\n" # Enables upgrading and downgrading the customer status.
        "5) Exit.\n"
        "\n" # Blank line for readability.
        "Your choice: "
        )

    option = expected_int(option) # All options are integers.

    if option == 1:
        if client.is_renting_a_car(): # Customer already has a car.
            print(
                "\nUnfortunately we only rent one car per customer.\n"
                f"We appreciate your compliance with the {shop.get_rental_shop_name()} company policy."
                )
        else:
            load()
            car_type = input("\nSelect car type: ").lower().title() # Ensure correct formatting.
            if car_type == "Suv": car_type = "SUV" # Special case as all letters are capital.

            if shop.is_available(car_type):
                num_days = input(
                    "For how many days do you want to rent?\n"
                    "Your choice: "
                    )
                num_days = expected_int(num_days) # Assumed integer number of days.
                car = shop.handout_car(car_type) # Retrieve car from shop stock.

                print("\nHanding the car over.")
                load()
                client.rent_car(car, car_type, num_days) # Provide car rental details to the customer.

                rate = shop.get_rate(car, num_days, client.is_vip())
                print(
                    f"You have rented a {car_type} car for {num_days} days.\n"
                    f"You will be charged £{rate} per day.\n"
                    "We hope that you enjoy our service!"
                    )
            else: # Car type unavailable, either not sold or not currently in stock.
                print(
                    f"\nUnfortunately no {car_type} is available.\n"
                    "We apologise for any inconvenience caused.\n"
                    "Please check our available cars to rent through the main menu."
                    )
   
        go_back() # Wait for user input to prooceed.

    elif option == 2:
        print("Checking available cars.")
        load()
        shop.display_stock() # Display stock of each car type and total stock.
        go_back()

    elif option == 3:
        details = client.return_car() # Retrieve rental details from the customer,
        car, car_type, num_days = details["car"], details["type"], details["days rented"]

        if shop.is_returnable(car_type, car): # Check if the car type is valid and can be returned.
            print("Retrieving the car.")
            load()

            print(
                "Thank you for returning the car to us!\n"
                "\n"
                "Calculating the bill."
                )
            load()

            rate = shop.get_rate(car, num_days, client.is_vip())
            price = shop.get_price(rate, num_days)
            # Display the bill.
            print(
                "####################BILL####################\n"
                f"You have rented a {car_type} car for {num_days} days.\n"
                f"Your daily rate is £{rate}.\n"
                f"Amount to pay: £{price}\n"
                "Please pay the amount online or in-store.\n"
                "############################################\n"
                "\n"
                "Thank you for using our service!\n"
                "Have a good day!"
                )
        else: # There is no car to return or the car type is invalid.
            print("\nUnfortunately you have no car to return.")
        
        go_back()

    elif option == 4: # Check or modify VIP status.
        print("\nRetrieving details.")
        load()

        if client.is_vip(): # Check if the customer is already a VIP.
            print(
                "You are part of our loyalty programme!\n"
                "Enjoy our discounted rental rates!"
                )
            
            # Offer option to leave the loyalty programme.
            downgrade = input("Press e to downgrade: ").lower()
            if downgrade == "e":
                print(f"Downgrading {client.get_customer_name()} and transferring details.")
                load()

                client = shop.downgrade(client) # Regular customer.
                go_back()
            else:
                load() # Pause briefly and go back to the main menu.

        else: # The customer has not signed up.
            print(
                "You have not signed up for the loyalty programme.\n"
                "Join us to access exclusive benefits, including discounted rates!"
                )
            
            # Offer option to sign up to the loyalty programme.
            upgrade = input("Press y to upgrade: ").lower()
            if upgrade == "y":
                print(f"Upgrading {client.get_customer_name()} and transferring details.")
                load()

                client = shop.upgrade(client) # VIP customer.
                go_back()
            else:
                load() # Pause briefly and go back to the main menu.

    elif option == 5: # Exit the program.
        shop.close_shop()
        load() # Short delay for friendly exit message.

    else: # Handle invalid options.
        print("Invalid option, choose between the available choices.")