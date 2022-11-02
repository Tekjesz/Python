def add(a: int, b: int) -> int:
    """
    Function to add two integers
    
    Args:
        a (int): first integer number to add
        b (int): second integer number to add
    Returns:
        sum (int): sum of a and b
    """
    # Add a and b
    sum = a + b
    
    # Return sum
    return sum

def multiply(a: int, b: int) -> int:
    """
    Function to multiply two integers
    
    Args:
        a (int): first integer number to multiply
        b (int): second integer number to multiply
    Returns:
        product (int): product of a and b
    """
    # Multiply a and b
    product = a * b
    
    # Return the product
    return product

if __name__ == "__main__":
    print(add(1, 2))
    print(multiply(1, 2))
    c = multiply(3, 4)