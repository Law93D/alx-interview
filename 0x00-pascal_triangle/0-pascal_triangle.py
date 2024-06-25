def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.

    Args:
    - n: An integer specifying the number of rows of Pascal's Triangle to generate.

    Returns:
    - A list of lists of integers representing Pascal's Triangle.
      Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row
    
    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]  # Each row starts with 1
        
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)  # Each row ends with 1
        triangle.append(new_row)
    
    return triangle

# Example usage and testing:
def print_triangle(triangle):
    """
    Prints the Pascal's Triangle.

    Args:
    - triangle: A list of lists of integers representing Pascal's Triangle.
    """
    for row in triangle:
        print("[{}]".format(",".join(map(str, row))))

if __name__ == "__main__":
    # Test case: Print Pascal's Triangle with 5 rows
    triangle = pascal_triangle(5)
    print_triangle(triangle)
