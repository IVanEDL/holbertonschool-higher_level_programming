#!/usr/bin/python3
"""Class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Yes, class rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if width <= 0:
            raise ValueError("width must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """calculates area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle"""
        for a in range(0, self.__y):
            print("")
        for i in range(0, self.__height):
            for az in range(0, self.__x):
                print(" ", end="")
            for p in range(0, self.__width):
                print('#', end="")
            print("")

    def __str__(self):
        """str method"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} "
                f"- {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """udpates the arguments of the rectangle"""
        if args and len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
            i = 0
            for argv in args:
                setattr(self, attributes[i], argv)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
