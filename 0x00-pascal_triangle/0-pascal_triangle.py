def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        # Start with a row of ones
        row = [1] * (i + 1)
        
        # Fill in the intermediate values
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle

# Main script to test the function
if __name__ == "__main__":
    def print_triangle(triangle):
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
