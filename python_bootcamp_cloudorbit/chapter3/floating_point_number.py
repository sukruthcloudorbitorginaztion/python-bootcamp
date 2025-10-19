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
        self.sign = -1 if number[0] == "-" else 1
        if "." not in number:
            self.integer_part = int(number.lstrip("-"))
            self.fraction_part = 0
        else:
            self.integer_part = int(number.lstrip("-").split(".")[0])
            fraction_part_str = number.split(".")[1].rstrip("0")
            self.fraction_part = (
                int(number.split(".")[1].rstrip("0")) if len(fraction_part_str) else 0
            )

    def __add__(self, right):
        """
        Add two floating numbers

        Args:
            right (floating_point_number or string which has floating point value): e.g "11.5"

        Returns:
            [floating_point_number]: returns the added value
        """
        right = FloatingPointNumber(str(right))

        left_len = len(str(self.fraction_part))
        right_len = len(str(right.fraction_part))
        max_len = max(left_len, right_len)

        left_fraction = 10 ** (max_len - left_len) * self.fraction_part
        right_fraction = 10 ** (max_len - right_len) * right.fraction_part

        left_number = int(f"{self.integer_part}{left_fraction}") * self.sign
        right_number = int(f"{right.integer_part}{right_fraction}") * right.sign

        total = left_number + right_number

        sign = 1
        if total < 0:
            total = total * -1
            sign = -1

        integer_part = total // 10 ** max_len
        fraction_part = total % 10 ** max_len

        if sign == -1:
            return FloatingPointNumber(f"-{integer_part}.{fraction_part}")
        else:
            return FloatingPointNumber(f"{integer_part}.{fraction_part}")

    def __sub__(self, right):
        """Subtract

        Args:
            right (floating_point_number or string which has floating values): [description]

        Returns:
            [floating_point_number]: returns the subtracted value
        """

        temp = FloatingPointNumber(str(right))
        temp.sign = temp.sign * -1

        return self + temp

    def __str__(self):
        """
        String conversion

        Returns:
            str: returns the string format
        """
        if self.sign == -1:
            return f"-{self.integer_part}.{self.fraction_part}"
        else:
            return f"{self.integer_part}.{self.fraction_part}"

    def __eq__(self, other):
        """
        Compare if both the floating point numbers are equal

        Args:
            other (bool): returns either true or false
        """
        return str(self) == str(other)

    def __ne__(self, other):
        """
        Compare if both the floating point numbers are not equal

        Args:
            other (bool): returns either true or false
        """
        return not (self == other)
