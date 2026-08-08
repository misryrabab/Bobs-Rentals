"""
Author: Rabab Misry
Course: Object-Oriented Programming
Final Project - Bob's Rentals

This file contains the Rental class.
"""


class Rental:
    """
    Represents a rental transaction.
    """

    def __init__(self, customer, equipment, rental_basis, rental_length, quantity):
        self._customer = customer
        self._equipment = equipment
        self._rental_basis = rental_basis
        self._rental_length = rental_length
        self._quantity = quantity

    @property
    def customer(self):
        return self._customer

    @property
    def equipment(self):
        return self._equipment

    @property
    def rental_basis(self):
        return self._rental_basis

    @property
    def rental_length(self):
        return self._rental_length

    @property
    def quantity(self):
        return self._quantity

    def calculate_cost(self):
        """
        Calculate the rental cost.
        """
        return self._equipment.calculate_price(
            self._rental_basis,
            self._rental_length
        ) * self._quantity