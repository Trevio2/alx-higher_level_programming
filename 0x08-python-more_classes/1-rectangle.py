#!/usr/bin/python3
"""This module is for the rectangle class"""


class Rectangle:
    """Class Rectangle that defines the object"""

    def __init__(self, width=0, height=0):
        """Initialize the object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for the width attribute"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for the height attribute"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value