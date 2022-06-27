#!/usr/bin/python3
"""
Define empty class Rectangle
"""


class Rectangle:
    """Representetion of Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize the Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Function to return instance of private width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        return self.__width = value

    @property
    def height(self):
        """Function to get instance of private instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        return self.__height == value
