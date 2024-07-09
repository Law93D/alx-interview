#!/usr/bin/python3
"""
Minimum Operations module
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters
    in the file.

    Args:
        n (int): The number of H characters to achieve.

    Returns:
        int: The minimum number of operations needed, or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return 0

    divisor = 2
    num_of_operations = 0

    while n > 1:
        if n % divisor == 0:
            print("Divisor is:", divisor)
            n = n // divisor  # Use integer division
            print("n = n / divisor:", n)
            num_of_operations += divisor
            print("Number of operations:", num_of_operations)
        else:
            divisor += 1
            print("Divisor after increment:", divisor)

    return num_of_operations

# Example usage
n = 12
print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
