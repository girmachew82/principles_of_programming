# standard
'''
the most familiar form, places no restrictions on the calling 
convention and arguments may be passed by position or keyword:
'''
def add(x, y): 
    '''
    Add two numbers.

    Parameter:
    x(int or float): The first number.
    y(int or float): The second number.

    Returns:
    int or float: The result of x plus y.

    Examples:
    >>> add(2, 2)
    4
    >>> add(2.5, 2)
    4.5
    '''
    return x + y

# position only
'''
restricted to only use positional parameters as there is a / in the function definition
'''
def sub(x, y,/ ) -> int: 
    '''
    Find difference of two numbers.

    Parameter:
    x(int): The subtract number.
    y(int): The subtracted number.

    Returns:
    int: The difference of x and y.

    Examples:
    >>> sub(2, 2)
    0
    >>> sub(-2, 2)
    -4
    '''
    return x - y
#keyword only
'''
only allows keyword arguments as indicated by a * in the function definition:
'''
def mul(*, x, y): 

    return x * y

#combination of positional and keyword arguments
# x is position and y can be either position or keyword
def div(x, /, y): 
  
    return x / y
# variable length of parameter
def sum(*x): 
    sum = 0
    for i in x:
        sum += i
    return sum
'''
x, y = 3, 4.0
print(f"{x} - {y} = {add(x, y)}") 
print(f"{10} - {10} = {add(x = 10, y = 10)}") 
print(f"{x} - {y} = {sub(x, y)}") 
print(f"{x} * {y} = {mul(x=2, y=2)}") 
print(f"{x} / {2} = {div(x, y=2)}") 
print(f"{x} / {y} = {div(x, y)}") 
'''