"""
Author: Rabab Misry
Course: Object-Oriented Programming
Final Project - Bob's Rentals

This file contains the RentalShop class.
"""

from datetime import datetime
from rental import Rental


class RentalShop:
    """
    Represents the rental shop.
    """

    def __init__(self):
        self._inventory = []
        self._active_rentals = []

    @property
    def inventory(self):
        return self._inventory

    @property
    def active_rentals(self):
        return self._active_rentals

    def add_equipment(self, equipment):
        """
        Adds equipment to the inventory.
        """
        self._inventory.append(equipment)

    def show_inventory(self):
        """
        Displays all available equipment.
        """
        print("\nAvailable Equipment")
        print("-------------------")

        for equipment in self._inventory:
            if equipment.available:
                equipment.display_information()
                print()

    def rent_equipment(self, customer, equipment,
                       rental_basis, rental_length, quantity):
        """
        Creates a rental if the equipment is available.
        """

        if not equipment.available:
            print("Sorry, this equipment is not available.")
            return None

        equipment.available = False

        customer.rental_basis = rental_basis
        customer.number_of_items = quantity
        customer.rental_time = datetime.now()

        rental = Rental(
            customer,
            equipment,
            rental_basis,
            rental_length,
            quantity
        )

        self._active_rentals.append(rental)

        print("Rental completed successfully.")

        return rental