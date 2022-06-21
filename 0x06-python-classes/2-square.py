#!/usr/bin/python3
"""define class Square"""


class Square:
    """Represents a square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """initializes the square

        Args:
            size (int): size of a side of the square

        Returns:
            None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")        
        elif:
            if size < 0:
                raise ValueError("ize must be >= 0")
            else:
                self.__size = size
