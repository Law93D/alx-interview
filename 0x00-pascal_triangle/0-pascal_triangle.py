def pascal_triangle(n):
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
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)
