"""
Author: Rabab Misry
Course: Object-Oriented Programming
Final Project - Bob's Rentals

This file contains the Customer class.
"""

from datetime import datetime


class Customer:
    """
    Represents a customer who rents equipment.
    """

    def __init__(self, customer_id, first_name, last_name):
        self._customer_id = customer_id
        self._first_name = first_name
        self._last_name = last_name

        self._rental_basis = ""
        self._number_of_items = 0
        self._rental_time = None

    # Properties

    @property
    def customer_id(self):
        return self._customer_id

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def rental_basis(self):
        return self._rental_basis

    @rental_basis.setter
    def rental_basis(self, value):
        self._rental_basis = value

    @property
    def number_of_items(self):
        return self._number_of_items

    @number_of_items.setter
    def number_of_items(self, value):
        self._number_of_items = value

    @property
    def rental_time(self):
        return self._rental_time

    @rental_time.setter
    def rental_time(self, value):
        self._rental_time = value

    def return_equipment(self):
        """
        Returns rental information needed by the rental shop.
        """

        if (
            self._rental_basis
            and self._number_of_items > 0
            and self._rental_time is not None
        ):

            return (
                self._rental_time,
                self._rental_basis,
                self._number_of_items
            )

        return None

    def display_customer(self):
        print("Customer ID:", self._customer_id)
        print("Name:", self._first_name, self._last_name)