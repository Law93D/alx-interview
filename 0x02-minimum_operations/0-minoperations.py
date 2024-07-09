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
        while n % divisor == 0:
            n //= divisor  # Use integer division
            num_of_operations += divisor
        divisor += 1

    return num_of_operations

# Example usage
if __name__ == "__main__":
    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
