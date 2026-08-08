"""
Author: Rabab Misry
Course: Object-Oriented Programming
Final Project - Bob's Rentals

This file contains the Ski class.
"""

from rental_equipment import RentalEquipment


class Ski(RentalEquipment):
    """
    Represents a pair of skis.
    """

    def __init__(self, equipment_id, equipment_name, rental_rate, ski_length):
        super().__init__(equipment_id, equipment_name, rental_rate)
        self._ski_length = ski_length

    @property
    def ski_length(self):
        return self._ski_length

    def display_information(self):
        super().display_information()
        print("Ski Length:", self._ski_length, "cm")