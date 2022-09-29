#!/usr/bin/python3
"""Rectangle Class
"""

from models.base import Base


class Rectangle(Base):
    """Define a Rectangle Class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialisation of Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): [description]. Defaults to 0.
            y (int, optional): [description]. Defaults to 0.
            id (int, optional): Rectangle identification. Defaults to None.
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Get width value
        
        Returns:
            int: private instance attribute width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set width value in private instance attribute 

        Args:
            value (int): width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height value

        Returns:
            int: private instance attribute height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set height value in private instance attribute

        Args:
            value (int): height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value is <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get x value

        Returns:
            int: private instance attribute x of rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """set x value in private instance attribute

        Args:
            value (int): x value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value is < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ get y

        Returns:
            int: private instance attribute y of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """set y value in private instance attribute

        Args:
            value (int): y value
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value is < 0:
            raise ValueError("y must be >=0")
        self.__y = value
