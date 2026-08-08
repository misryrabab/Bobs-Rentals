"""
Author: Rabab Misry
Course: Object-Oriented Programming
Final Project - Bob's Rentals

This file contains the RentalEquipment class.
"""

class RentalEquipment:
    """
    Base class for all rental equipment.
    """

    def __init__(self, equipment_id, equipment_name, rental_rate):
        self._equipment_id = equipment_id
        self._equipment_name = equipment_name
        self._rental_rate = rental_rate
        self._available = True

    # Properties

    @property
    def equipment_id(self):
        return self._equipment_id

    @property
    def equipment_name(self):
        return self._equipment_name

    @property
    def rental_rate(self):
        return self._rental_rate

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        self._available = value

    # Methods

    def display_information(self):
        print("Equipment ID:", self._equipment_id)
        print("Equipment Name:", self._equipment_name)
        print("Rental Rate: $", self._rental_rate)
        print("Available:", self._available)

    def calculate_price(self, rental_basis, rental_length):
        """
        Calculates the rental price.
        """

        if rental_basis == "hour":
            return self._rental_rate * rental_length

        elif rental_basis == "day":
            return (self._rental_rate * 8) * rental_length

        elif rental_basis == "week":
            return (self._rental_rate * 8 * 7) * rental_length

        else:
            return 0