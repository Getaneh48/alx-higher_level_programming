#!/usr/bin/python3
"""a module that defines a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """A class that represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # width getter
    @property
    def width(self):
        """Returns the width of the rectangle"""
        return self.__width

    # height getter
    @property
    def height(self):
        """Returns the height of the rectangle"""
        return self.__height

    # x getter
    @property
    def x(self):
        """Returns the x value of the rectangle"""
        return self.__x

    # y getter
    @property
    def y(self):
        """Returns the y value of the rectangle"""
        return self.__y

    # width setter
    @width.setter
    def width(self, width):
        """sets the width of the rectangle
        Args:
            width: width of the rectangle
        """
        if not type(width) is int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    # height setter
    @height.setter
    def height(self, height):
        """sets the height of the rectangle
        Args:
            height: height of the rectangle
        """
        if not type(height) is int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    # x value setter
    @x.setter
    def x(self, x):
        """sets the value of x
        Args:
            x: int value
        """
        if not type(x) is int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    # y value setter
    @y.setter
    def y(self, y):
        """sets the value of y
        Args:
            y: int value
        """
        if not type(y) is int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Displays the rectangle"""
        for y in range(self.__y):
            print()
        for r in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """returns the string representation of the rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Method that changed the order of arguments for rectangle object
        Args:
           *args: list of arguments
           **kwargs: Dictionary with arguments
        Return:
           Always nothing
        """
        dict_order = ['id', 'width', 'height', 'x', 'y']
        if args is not None and bool(args) is True:
            i = 0
            for key in dict_order:
                try:
                    setattr(self, key, args[i])
                except IndexError:
                    pass
                i += 1
        else:
            for key in dict_order:
                try:
                    setattr(self, key, kwargs[key])
                except KeyError:
                    pass

    def to_dictionary(self):
        """Method that returns a dictionary with
           attributes of the object.
        """
        dict_order = ['x', 'y', 'id', 'height', 'width']
        dict_attrs = {}
        for key in dict_order:
            dict_attrs[key] = getattr(self, key)
        return dict_attrs
