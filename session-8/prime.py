from typing import Union
def is_prime(n: Union[int, str]) -> bool:
    """
    Check if a number is a prime number.

    This function determines whether a given number is a prime.
    It accepts either an integer or a string that can be converted to an integer.
    Raises:
        ValueError: If the input is a string that cannot be converted to an integer.
        TypeError: If the input is neither an integer nor a convertible string.
    
    Parameters:
    n : int or str
        The number to check for primality.

    Returns:
    bool
        True if the number is prime, False otherwise.

    Example:
    -------
    >>> is_prime(7)
    True
    >>> is_prime("11")
    True
    >>> is_prime("not_a_number")
    ValueError: Cannot convert string to integer
    """
    if isinstance(n, str):
        try:
            n = int(n)
        except ValueError:
            raise ValueError("Cannot convert string to integer")

    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True
