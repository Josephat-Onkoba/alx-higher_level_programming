#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""
    
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square."""
        self.size = size
        self.position = position
    
    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    @property
    def position(self):
        """Get/set the position of the square."""
        return self.__position
    
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 \
           or not all(isinstance(val, int) for val in value) \
           or any(val < 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    
    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
    
    def my_print(self):
        """Print the square using '#' characters."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
