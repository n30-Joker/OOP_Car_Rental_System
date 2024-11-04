from customer import Customer
from rental_shops import RentalShop
import time


def expected_int(answer):
    correct = False
    while not correct:
        try:
            answer = int(answer)
        except ValueError:
            answer = input(
                "You should enter a number, try again.\n"
                "Your choice: "
                )
        else:
            correct = True
    
    return answer


def go_back():
    input("\n(Press any key to go back.)")


client = Customer("Tarek")

shop = RentalShop("RentACar")
shop.add_to_stock("Hatchback", 4)
shop.add_to_stock("Sedan", 3)
shop.add_to_stock("SUV", 3)

open = True

print(f"Welcome to {shop.get_name()}!")
time.sleep(2)

while open:
    option = input(
        f"\n{client.get_name()}, what would you like to do?\n"
        "1) Rent a car.\n"
        "2) Check available cars.\n"
        "3) Return car.\n"
        "4) Loyalty programme.\n"
        "5) Exit.\n"
        "\n"
        "Your choice: "
        )

    option = expected_int(option)
    print(" ")
    if option == 1:
        if client.car_rented():
            print(
                "Unfortunately we only rent one car per customer.\n"
                "We appreciate you wanting to use our service!"
                )
        else:
            car_type = input("Select car type: ").lower().title()
            if car_type == "Suv": car_type = "SUV"

            if shop.available(car_type):
                num_days = input(
                    "For how many days do you want to rent?\n"
                    "Your choice: "
                    )
                num_days = expected_int(num_days)
                car = shop.give_the_car(car_type)
                rate = shop.get_rate(car, num_days, client.vip_status())
                print(
                    f"You have rented a {car_type} car for {num_days} days.\n"
                    f"You will be charged £{rate} per day.\n"
                    "We hope that you enjoy our service."
                    )
                client.rent_car(car, car_type, num_days)
            else:
                print(
                    f"Unfortunately no {car_type} is available.\n"
                    "We apologise for any inconvenience caused."
                    )
                
        go_back()

    elif option == 2:
        shop.get_stock()
        go_back()

    elif option == 3:
        details = client.return_car()
        car, car_type, num_days = details["car"], details["type"], details["days"]
        if shop.return_car(car_type, car):
            rate = shop.get_rate(car, num_days, client.vip_status())
            price = shop.get_price(rate, num_days)
            print(
                "Thank you for returning the car to us!\n"
                f"You have rented a {car_type} car for {num_days} days.\n"
                f"Your daily rate is £{rate}.\n"
                f"Amount to pay: £{price}\n"
                "Please pay the amount online or in-store.\n"
                "Thank you for using our service!\n"
                "Have a good day!"
                )
        else:
            print("Unfortunately you have no car to return.")
        
        go_back()

    elif option == 4:
        if client.vip_status():
            print(
                "You are part of our loyalty programme!\n"
                "Enjoy our discounted rental rates!"
                )
            downgrade = input("Press e to downgrade: ").lower()
            if downgrade == "e":
                client = shop.downgrade(client)
                go_back()
            else:
                time.sleep(2)
        else:
            print(
                "You have not signed up for the loyalty programme.\n"
                "Join us to access exclusive benefits, including discounted rates!"
                )
            upgrade = input("Press y to upgrade: ").lower()
            if upgrade == "y":
                client = shop.upgrade(client)
                go_back()
            else:
                time.sleep(2)

    elif option == 5:
        print("Thank you for stopping by! See you soon!")
        time.sleep(2)
        open = False

    else:
        print("Invalid option, choose between the available choices.")