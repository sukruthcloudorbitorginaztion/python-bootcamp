"""
FloatingPointNumber
-------------------
Supports addition, subtraction and comparision  operator with highest accuracy
"""


class FloatingPointNumber:
    """
    FloatingPointNumber
    """

    def __init__(self, number):
        """Init

        Args:
            number (string): floating point numbers in strings. e. 123.1234567812345678
        """
        pass

    def __add__(self, right):
        """
        Add two floating numbers

        Args:
            right (floating_point_number or string which has floating point value): e.g "11.5"

        Returns:
            [floating_point_number]: returns the added value
        """
        pass

    def __sub__(self, right):
        """Subtract

        Args:
            right (floating_point_number or string which has floating values): [description]

        Returns:
            [floating_point_number]: returns the subtracted value
        """
        pass


    def __str__(self):
        """
        String conversion

        Returns:
            str: returns the string format
        """
        pass

    def __eq__(self, other):
        """
        Compare if both the floating point numbers are equal

        Args:
            other (bool): returns either true or false
        """
        pass

    def __ne__(self, other):
        """
        Compare if both the floating point numbers are not equal

        Args:
            other (bool): returns either true or false
        """
        pass
