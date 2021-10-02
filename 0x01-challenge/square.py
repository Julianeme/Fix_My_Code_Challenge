#!/usr/bin/python3
"""
Definition of square class and its methods
"""


class square():
    """
    definition of square class
    """
    width = 0

    def __init__(self, *args, **kwargs):
        """constructor"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter of the square """
        return (self.width * 4)

    def __str__(self):
        """Magic method str"""
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main__":

    s = square(width=12)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
