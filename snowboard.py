"""
Author: Rabab Misry
Course: Object-Oriented Programming
Final Project - Bob's Rentals

This file contains the Snowboard class.
"""

from rental_equipment import RentalEquipment


class Snowboard(RentalEquipment):
    """
    Represents a snowboard.
    """

    def __init__(self, equipment_id, equipment_name, rental_rate, board_size):
        super().__init__(equipment_id, equipment_name, rental_rate)
        self._board_size = board_size

    @property
    def board_size(self):
        return self._board_size

    def display_information(self):
        super().display_information()
        print("Board Size:", self._board_size, "cm")