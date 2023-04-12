#!/usr/bin/python3
"""This class that raises an Exception with the message if not implemented"""


class BaseGeometry:
    def area(self):
        """This module raises an Exception with a message"""
        raise TypeError("area() is not implemented")
