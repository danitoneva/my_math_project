"""
Math modile that makes math operations.
"""

class MathModule:
    """
    Math class that makes math operations.
    """

    @staticmethod
    def add_two_numbers(number1: int,number2: int) -> int:
        """
        Adds two numbers

        :parameter number1: first number
        :parameter number2: second number
        :return: sum of two numbers
        """
        return number1 + number2

    @staticmethod
    def subtract_two_numbers(number1: int,number2: int) -> int:
        """
        Subtracts two numbers

        :parameter number1: first number
        :parameter number2: second number
        :return: subtract of two numbers
        """
        return number1 - number2

    @staticmethod
    def multiply_two_numbers(number1: int,number2: int) -> int:
        """
        Multiplies two numbers

        :parameter number1: first number
        :parameter number2: second number
        :return: multiply of two numbers
        """
        return number1 * number2    

    @staticmethod
    def divide_two_numbers(number1: float,number2: float) -> float:
        """
        Divides two numbers

        :parameter number1: first number
        :parameter number2: second number
        :return: divide of two numbers
        """
        try:
            return number1 / number2
        except ZeroDivisionError as e:
            raise ZeroDivisionError("Error: Division by zero is not allowed.") from e
