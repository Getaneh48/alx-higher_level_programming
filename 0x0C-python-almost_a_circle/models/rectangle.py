#!/usr/bin/python3
from models.base import Base

"""
defines a rectangle class
"""


class Rectangle(Base):
    """
    a rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        gets the width of a rectangle

        Returns:
            int: width of a rectangle
        """
        return self.__width

    @property
    def height(self):
        """
        gets the heights of a rectangle

        Returns:
            int: height of a rectangle
        """
        return self.__height

    @property
    def x(self):
        """
        gets the x value of a rectangle

        Returns:
            int: x value of a rectangle
        """
        return self.__x

    @property
    def y(self):
        """
        gets the y value of a rectangle

        Returns:
            int: y value of a rectangle
        """
        return self.__y

    @width.setter
    def width(self, value):
        """
        Given a value, sets the width of a rectangle

        Args:
            int: width of a rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        Given a value, sets the height of a rectangle

        Args:
            int: height of a rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        Given a value, sets the x value of a rectangle

        Args:
            int: x value of a rectangle
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise TypeError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        Given a value, sets the y value of a rectangle

        Args:
            int: y value of a rectangle
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise TypeError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Calculates the area of a rectangle

        Returns:
            int: the area of a rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        print in stdout the Rectangle instance with the
        character # by taking care of x and y
        """
        for y in range(0, self.__y):
            print(end="\n")
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(end=" ")
            for j in range(0, self.__width):
                print("#", end="")
            if i < self.__height:
                print(end="\n")

    def __str__(self):
        """
        Generates string representation of a class

        Returns:
            str: string representation of a class
        """
        x = self.x
        y = self.y
        width = self.width
        height = self.height

        return f"[Rectangle] ({self.id}) {x}/{y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of an instance based on the given parameters

        Args:
            list: list of attribute values
            dict: dictionary of keyword attributes
        """
        if len(args) > 0:
            ls = ['id', 'width', 'height', 'x', 'y']
            for i in range(0, len(args)):
                setattr(self, ls[i], args[i])
        else:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """
        Generates dictionary representation the object

        Returns:
            dict: dictionary representation of the object
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'width': self.width, 'height': self.height}


if __name__ == "__main__":
    pass
