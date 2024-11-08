from customer import Customer
from rental_shops import RentalShop
import time


def expected_int(answer):
    """
    Validates the user input to ensure it can be converted
    to an integer. If the input is not an integer, it requests
    the user to re-enter a valid number.

    Assumptions:
        The function will keep on running until the user enters
        a number.

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
                "You should enter a number, try again.\n"
                "Your choice: "
                )
        else:
            correct = True # Exit the loop.
    
    return answer


def go_back():
    """
    Pauses the program until the user presses any key to proceed.
    Useful for providing the user with time to read messages.
    """
    input("\n(Press any key to go back.)")


# Instantiate a new regular customer named 'TestCustomer'
client = Customer("TestCustomer")

# Create a new rental shop named 'RentACar'.
# Add cars to the shop's inventory.
# Currently only 3 types of cars available: hatchback, sedan and SUV
shop = RentalShop("RentACar")
shop.add_to_stock("Hatchback", 4)
shop.add_to_stock("Sedan", 3)
shop.add_to_stock("SUV", 3) # Can add more types later on.

open = True

print(f"Welcome to {shop.get_name()}!")
time.sleep(2) # Short pause for beter user experience,

# Main program loop.
while open:
    option = input(
        f"\n{client.get_name()}, what would you like to do?\n"
        "1) Rent a car.\n"
        "2) Check available cars.\n"
        "3) Return car.\n"
        "4) Loyalty programme.\n" # Enables upgrading and downgrading the customer status.
        "5) Exit.\n"
        "\n"
        "Your choice: "
        )

    option = expected_int(option) # All options are integers.
    print(" ")

    if option == 1:
        if client.car_rented(): # Customer already has a car.
            print(
                "Unfortunately we only rent one car per customer.\n"
                "We appreciate you wanting to use our service!"
                )
        else:
            car_type = input("Select car type: ").lower().title() # Ensure correct formatting.
            if car_type == "Suv": car_type = "SUV" # Special case as all letters are capital.

            if shop.available(car_type):
                num_days = input(
                    "For how many days do you want to rent?\n"
                    "Your choice: "
                    )
                num_days = expected_int(num_days) # Assumed integer number of days.
                car = shop.give_the_car(car_type) # Retrieve car from shop stock.
                rate = shop.get_rate(car, num_days, client.vip_status())
                print(
                    f"You have rented a {car_type} car for {num_days} days.\n"
                    f"You will be charged £{rate} per day.\n"
                    "We hope that you enjoy our service."
                    )
                client.rent_car(car, car_type, num_days) # Provide car rental details to the customer.
            else: # Car type unavailable, either not sold or not currently in stock.
                print(
                    f"Unfortunately no {car_type} is available.\n"
                    "We apologise for any inconvenience caused."
                    )
   
        go_back() # Wait for user input to prooceed.

    elif option == 2:
        shop.get_stock() # Display stock of each car type and total stock.
        go_back()

    elif option == 3:
        details = client.return_car() # Retrieve rental details from the customer,
        car, car_type, num_days = details["car"], details["type"], details["days"]

        if shop.return_car(car_type, car): # Check if the car type is valid and can be returned.
            rate = shop.get_rate(car, num_days, client.vip_status())
            price = shop.get_price(rate, num_days)
            # Display the bill.
            print(
                "Thank you for returning the car to us!\n"
                f"You have rented a {car_type} car for {num_days} days.\n"
                f"Your daily rate is £{rate}.\n"
                f"Amount to pay: £{price}\n"
                "Please pay the amount online or in-store.\n"
                "Thank you for using our service!\n"
                "Have a good day!"
                )
        else: # There is no car to return or the car type is invalid.
            print("Unfortunately you have no car to return.")
        
        go_back()

    elif option == 4: # Check or modify VIP status.
        if client.vip_status(): # Check if the customer is already a VIP.
            print(
                "You are part of our loyalty programme!\n"
                "Enjoy our discounted rental rates!"
                )
            
            # Offer option to leave the loyalty programme.
            downgrade = input("Press e to downgrade: ").lower()
            if downgrade == "e":
                client = shop.downgrade(client) # Regular customer.
                go_back()
            else:
                time.sleep(2) # Pause briefly and go back to the main menu.

        else: # The customer has not signed up.
            print(
                "You have not signed up for the loyalty programme.\n"
                "Join us to access exclusive benefits, including discounted rates!"
                )
            
            # Offer option to sign up to the loyalty programme.
            upgrade = input("Press y to upgrade: ").lower()
            if upgrade == "y":
                client = shop.upgrade(client) # VIP customer.
                go_back()
            else:
                time.sleep(2) # Pause briefly and go back to the main menu.

    elif option == 5: # Exit the program.
        print("Thank you for stopping by! See you soon!")
        time.sleep(2) # Short delay for friendly exit message.
        open = False

    else: # Handle invalid options.
        print("Invalid option, choose between the available choices.")