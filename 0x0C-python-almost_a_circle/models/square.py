#!/usr/bin/python3
"""
Defines a Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        string representation of the class

        Returns:
            str: string representation of the class
        """
        x = self.x
        y = self.y
        width = self.width

        return f"[Square] ({self.id}) {x}/{y} - {width}"

    @property
    def size(self):
        """
        Gets the size of the square class

        Returns:
            int: size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Given a value, sets the size of the square class

        Args:
            value(int): size of the square class
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Based on the two arguments, updates the attributes of the current
        instance

        Args:
            args(list): variable length of instance attribute values
            kwargs(dict): variable length of dictionary of attribute:value
        """
        if args is not None and len(args) > 0:
            ls = ['id', 'size', 'x', 'y']
            for i in range(0, len(args)):
                setattr(self, ls[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        generates dictionary reprsentation of the current instance

        Returns:
            dict: dictionary of instance attributes and their value
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

if __name__ == "__main__":
    pass
