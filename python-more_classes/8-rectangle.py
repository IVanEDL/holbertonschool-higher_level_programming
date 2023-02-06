#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """yes. Rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initialization method. Cash and money."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @width.setter
    def width(self, width):
        """width setter"""
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @height.setter
    def height(self, height):
        """height setter"""
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        """print method by print()"""
        if self.__height == 0 or self.__width == 0:
            return ""
        temp = []
        for i in range(self.__height):
            if i > 0:
                temp.append("\n")
            for p in range(self.__width):
                temp.append(str(self.print_symbol))
        return "".join(temp)

    def __repr__(self):
        """repr method"""
        return ("Rectangle(" + str(self.__width) + ", " +
                str(self.__height) + ")")

    def __del__(self):
        """message put when object deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the bigger rectangle BASED (on area)"""
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
