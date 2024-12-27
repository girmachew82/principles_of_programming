def add(x, y):
    """
    Add two numbers together.

    Parameters:
    x (int or float): The first number.
    y (int or float): The second number.

    Returns:
    int or float: The sum of x and y.

    Example:
    >>> add(3, 4)
    7
    >>> add(3.5, 2.5)
    6.0
    """
    return x + y

def sub(x: int, y: int) -> int:
    """
    Subtract one integer from another.

    Parameters:
    x (int): The number to be subtracted from.
    y (int): The number to subtract.

    Returns:
    int: The difference between x and y.

    Example:
    >>> sub(10, 3)
    7
    >>> sub(5, 10)
    -5
    """
    return x - y

def mul(x, y):
    """
    Multiply two numbers.

    Parameters:
    x (int or float): The first number.
    y (int or float): The second number.

    Returns:
    int or float: The product of x and y.

    Example:
    >>> mul(3, 4)
    12
    >>> mul(2.5, 4)
    10.0
    """
    return x * y


def div(x, y):
    """
    Divide one number by another.

    Parameters:
    x (int or float): The numerator.
    y (int or float): The denominator.

    Returns:
    float: The result of the division.

    Raises:
    ZeroDivisionError: If the denominator is zero.

    Example:
    >>> div(10, 2)
    5.0
    >>> div(3, 2)
    1.5
    """
    return x / y


x, y = 3, 4.0
print(f"{x} - {y} = {sub(x, y)}")