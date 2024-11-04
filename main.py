from customer import Customer
from rental_shops import RentalShop
import time
    
def expectedInt(answer):
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

def goBack():
    input("\n(Press any key to go back.)")

client = Customer("Tarek")

shop = RentalShop("RentACar")
shop.addToStock("Hatchback", 4)
shop.addToStock("Sedan", 3)
shop.addToStock("SUV", 3)

open = True

print(f"Welcome to {shop.getName()}!")
time.sleep(2)

while open:
    option = input(
        f"\n{client.getName()}, what would you like to do?\n"
        "1) Rent a car.\n"
        "2) Check available cars.\n"
        "3) Return car.\n"
        "4) Loyalty programme.\n"
        "5) Exit.\n"
        "\n"
        "Your choice: "
        )

    option = expectedInt(option)
    print(" ")
    if option == 1:
        if client.carRented():
            print(
                "Unfortunately we only rent one car per customer.\n"
                "We appreciate you wanting to use our service!"
                )
        else:
            carType = input("Select car type: ").lower().title()
            if carType == "Suv": carType = "SUV"
            if shop.available(carType):
                numDays = input(
                    "For how many days do you want to rent?\n"
                    "Your choice: "
                    )
                numDays = expectedInt(numDays)
                car = shop.giveTheCar(carType)
                rate = shop.getRate(car, numDays, client.VIPStatus())
                print(
                    f"You have rented a {carType} car for {numDays} days.\n"
                    f"You will be charged £{rate} per day.\n"
                    "We hope that you enjoy our service."
                    )
                client.rentCar(car, carType, numDays)
            else:
                print(
                    f"Unfortunately no {carType} is available.\n"
                    "We apologise for any inconvenience caused."
                    )
                
        goBack()

    elif option == 2:
        shop.getStock()
        goBack()

    elif option == 3:
        details = client.returnCar()
        car, carType, numDays = details["car"], details["type"], details["days"]
        if shop.returnCar(carType, car):
            rate = shop.getRate(car, numDays, client.VIPStatus())
            price = shop.getPrice(rate, numDays)
            print(
                "Thank you for returning the car to us!\n"
                f"You have rented a {carType} car for {numDays} days.\n"
                f"Your daily rate is £{rate}.\n"
                f"Amount to pay: £{price}\n"
                "Please pay the amount online or in-store.\n"
                "Thank you for using our service!\n"
                "Have a good day!"
                )
        else:
            print("Unfortunately you have no car to return.")
        
        goBack()

    elif option == 4:
        if client.VIPStatus():
            print(
                "You are part of our loyalty programme!\n"
                "You have access to discounted rental rates."
                )
            downgrade = input("Press e to downgrade: ").lower()
            if downgrade == "e":
                client = shop.downgrade(client)
                goBack()
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
                goBack()
            else:
                time.sleep(2)

    elif option == 5:
        print("Thank you for stopping by! See you soon!")
        time.sleep(2)
        open = False

    else:
        print("Invalid option, choose between the available choices.")