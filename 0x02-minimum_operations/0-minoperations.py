"""
In a text file, there is a single character 'H'.
Your text editor can execute only two operations in
this file: 'copy All' and 'paste'.
Given a number n, write a method that calculate the
fewest number of operations needed to result in
exactly 'n' 'H' characters in the file.

program will return an integer.
If 'n' is impossible to achieve, return '0'
"""

def minOperations(n):
    if n <= 1:
        return 0

    divisor = 2

    num_of_operations = 0
    
    while n > 1:
        if n % divisor == 0:
            print("divisor is: ", divisor)
            n = n / divisor
            print("\nn = n / divisor", n)

            num_of_operations = num_of_operations = divisor
            print("\nnum of ops", num_of_operations)

        else:
            divisor += 1
            print("divisor after increament: ", divisor)

    return num_of_operations

n = 12

print(minOperations(n))
