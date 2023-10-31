#!/usr/bin/python3

"""Defines class Rectangle."""

class Rectangle:
    """Represents a rectangle. Nil body.

    Attributes:
        number_of_instances (int): number of Rectangle instances.
        print_symbol (any): symbol used for string representation."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize new Rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Return width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of the rectangle. """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2*(self.__width + self.__height))

    def __str__(self):
        """Return printable representation of the Rectangle.

        Represents rectangle with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append('\n')
        return ("".join(rect))

    def __repr__(self):
        """Return string representation of the rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
