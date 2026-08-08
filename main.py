"""
Author: Rabab Misry
Course: Object-Oriented Programming
Final Project - Bob's Rentals

Main program to test the rental system.
"""

from rental_shop import RentalShop
from customer import Customer
from ski import Ski
from snowboard import Snowboard


def main():

    # Create rental shop
    shop = RentalShop()

    # Create equipment
    ski1 = Ski(1, "Rossignol Skis", 20, 170)
    snowboard1 = Snowboard(2, "Burton Snowboard", 25, 160)

    # Add equipment
    shop.add_equipment(ski1)
    shop.add_equipment(snowboard1)

    # Create customer
    customer = Customer(1, "John", "Smith")

    # Display equipment
    shop.show_inventory()

    # Rent skis
    rental = shop.rent_equipment(
        customer,
        ski1,
        "day",
        3,
        1
    )

    if rental:
        print()
        print("Total Cost: $", rental.calculate_cost())


if __name__ == "__main__":
    main()
