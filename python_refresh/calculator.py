def add(a: float, b: float) -> float:
    '''This function takes two numbers and returns their sum.'''
    return sum([a,b])

def subtract(a: float, b: float) -> float:
    '''This function takes two numbers and returns their difference.'''
    return a - b

def multiply(a: float, b: float) -> float:
    '''This function takes two numbers and returns their product.'''
    return a * b

def divide(a: float, b: float) -> float:
    '''This function takes two numbers and returns their quotient.'''
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b